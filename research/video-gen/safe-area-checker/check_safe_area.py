#!/usr/bin/env python3
"""Check a 1080x1920 video for colored content outside a safe rectangle and small text.

Requires only Python's standard library, OpenCV (cv2), and NumPy.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np

VIDEO_W, VIDEO_H = 1080, 1920
SAFE_RECT = (48, 288, 888, 1248)  # inclusive x1,y1,x2,y2


def parse_hex_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("color must be six hex digits, e.g. F4F1E8")
    try:
        rgb = tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("color must be six hex digits") from exc
    return (rgb[2], rgb[1], rgb[0])  # OpenCV uses BGR


def group_text_lines(mask: np.ndarray, min_area: int, max_gap: int) -> list[dict]:
    """Approximate text-line boxes by joining nearby dark connected components."""
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    boxes = []
    for i in range(1, count):
        x, y, w, h, area = map(int, stats[i])
        if area >= min_area and h >= 4 and w >= 1:
            boxes.append([x, y, x + w, y + h])  # half-open for box dimensions
    if not boxes:
        return []

    # Union nearby components on the same text line. The vertical overlap check
    # prevents adjacent lines from being merged; the gap handles spaces.
    parent = list(range(len(boxes)))

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, a in enumerate(boxes):
        ax1, ay1, ax2, ay2 = a
        ah = ay2 - ay1
        for j in range(i + 1, len(boxes)):
            b = boxes[j]
            bx1, by1, bx2, by2 = b
            overlap = max(0, min(ay2, by2) - max(ay1, by1))
            min_h = min(ah, by2 - by1)
            gap = max(0, max(ax1, bx1) - min(ax2, bx2))
            if overlap >= max(2, int(0.25 * min_h)) and gap <= max_gap:
                union(i, j)

    groups: dict[int, list[list[int]]] = {}
    for i, box in enumerate(boxes):
        groups.setdefault(find(i), []).append(box)

    lines = []
    for members in groups.values():
        x1 = min(b[0] for b in members)
        y1 = min(b[1] for b in members)
        x2 = max(b[2] for b in members)
        y2 = max(b[3] for b in members)
        lines.append({"bbox": [x1, y1, x2, y2], "height_px": y2 - y1,
                      "component_count": len(members)})
    return sorted(lines, key=lambda item: (item["bbox"][1], item["bbox"][0]))


def analyze_frame(frame: np.ndarray, args: argparse.Namespace) -> dict:
    # Compare each pixel with the configured flat pale-background color in Lab.
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB).astype(np.int16)
    bg_lab = cv2.cvtColor(np.uint8([[args.background]]), cv2.COLOR_BGR2LAB)[0, 0].astype(np.int16)
    delta = np.sqrt(np.sum((lab - bg_lab) ** 2, axis=2))
    foreground = delta > args.background_tolerance

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    colored = foreground & (hsv[:, :, 1] >= args.min_saturation)

    x1, y1, x2, y2 = args.safe_rect
    outside = np.ones((VIDEO_H, VIDEO_W), dtype=bool)
    outside[y1:y2 + 1, x1:x2 + 1] = False
    outside_colored = int(np.count_nonzero(colored & outside))
    outside_foreground = int(np.count_nonzero(foreground & outside))

    tx1, ty1, tx2, ty2 = args.text_roi
    gray = cv2.cvtColor(frame[ty1:ty2, tx1:tx2], cv2.COLOR_BGR2GRAY)
    dark = (gray <= args.dark_threshold).astype(np.uint8)
    # A small horizontal close helps join broken strokes without OCR or scaling.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    dark = cv2.morphologyEx(dark, cv2.MORPH_CLOSE, kernel)
    lines = group_text_lines(dark, args.min_component_area, args.line_gap)
    for line in lines:
        bx1, by1, bx2, by2 = line["bbox"]
        line["bbox"] = [bx1 + tx1, by1 + ty1, bx2 + tx1, by2 + ty1]
        line["below_minimum"] = line["height_px"] < args.min_text_height

    return {
        "outside_colored_pixels": outside_colored,
        "outside_non_background_pixels": outside_foreground,
        "small_text_lines": [line for line in lines if line["below_minimum"]],
        "text_lines": lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="1080x1920 MP4 input")
    parser.add_argument("--background", type=parse_hex_color, default=parse_hex_color("F4F1E8"),
                        help="flat pale background RGB hex (default: F4F1E8)")
    parser.add_argument("--background-tolerance", type=float, default=18.0,
                        help="Lab color distance above which a pixel is foreground (default: 18)")
    parser.add_argument("--min-saturation", type=int, default=35,
                        help="HSV saturation threshold for colored/essential pixels, 0-255 (default: 35)")
    parser.add_argument("--safe-rect", nargs=4, type=int, metavar=("X1", "Y1", "X2", "Y2"),
                        default=SAFE_RECT, help="inclusive safe rectangle (default: 48 288 888 1248)")
    parser.add_argument("--text-roi", nargs=4, type=int, metavar=("X1", "Y1", "X2", "Y2"),
                        default=(48, 288, 889, 1249),
                        help="half-open OCR-free text scan region (default: safe rectangle)")
    parser.add_argument("--dark-threshold", type=int, default=105,
                        help="grayscale threshold for dark text (default: 105)")
    parser.add_argument("--min-text-height", type=int, default=40,
                        help="flag estimated text-line boxes below this height in pixels (default: 40)")
    parser.add_argument("--min-component-area", type=int, default=3,
                        help="ignore dark connected components smaller than this area (default: 3)")
    parser.add_argument("--line-gap", type=int, default=24,
                        help="maximum horizontal gap when grouping same-line text components (default: 24)")
    parser.add_argument("--json-out", type=Path, help="also write complete report to this JSON file")
    args = parser.parse_args()

    if not 0 <= args.min_saturation <= 255 or not 0 <= args.dark_threshold <= 255:
        parser.error("saturation and dark thresholds must be between 0 and 255")
    for name, rect in (("safe rectangle", args.safe_rect), ("text ROI", args.text_roi)):
        x1, y1, x2, y2 = rect
        if not (0 <= x1 < x2 <= VIDEO_W and 0 <= y1 < y2 <= VIDEO_H):
            parser.error(f"{name} must be an increasing rectangle within 1080x1920")

    cap = cv2.VideoCapture(str(args.video))
    if not cap.isOpened():
        print(f"ERROR: cannot open video: {args.video}", file=sys.stderr)
        return 2
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if (width, height) != (VIDEO_W, VIDEO_H):
        cap.release()
        print(f"ERROR: expected 1080x1920 video, got {width}x{height}", file=sys.stderr)
        return 2

    report = {"video": str(args.video), "width": width, "height": height,
              "safe_rect_inclusive": args.safe_rect, "frames_checked": 0,
              "frames_with_outside_color": [], "frames_with_small_text": [],
              "frame_results": []}
    frame_no = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        result = analyze_frame(frame, args)
        result["frame"] = frame_no
        report["frames_checked"] += 1
        if result["outside_colored_pixels"]:
            report["frames_with_outside_color"].append(frame_no)
        if result["small_text_lines"]:
            report["frames_with_small_text"].append(frame_no)
        if result["outside_colored_pixels"] or result["small_text_lines"]:
            report["frame_results"].append(result)
        frame_no += 1
    cap.release()

    if frame_no == 0:
        print("ERROR: video contains no decodable frames", file=sys.stderr)
        return 2
    print(f"Checked {frame_no} frames ({width}x{height}).")
    print(f"Frames with colored pixels outside safe area: {len(report['frames_with_outside_color'])}")
    print(f"Frames with estimated text lines under {args.min_text_height}px: {len(report['frames_with_small_text'])}")
    for result in report["frame_results"]:
        if result["outside_colored_pixels"]:
            print(f"  frame {result['frame']}: {result['outside_colored_pixels']} colored pixels outside; "
                  f"{result['outside_non_background_pixels']} total non-background pixels outside")
        for line in result["small_text_lines"]:
            print(f"  frame {result['frame']}: small text-line estimate {line['height_px']}px at {line['bbox']}")
    if args.json_out:
        args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Full issue-frame report: {args.json_out}")
    return 1 if report["frames_with_outside_color"] or report["frames_with_small_text"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
