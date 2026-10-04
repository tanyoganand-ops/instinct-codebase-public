# Safe-area and text-size check

`check_safe_area.py` scans **every frame** of a 1080x1920 MP4. It compares pixels with a configurable flat pale background in Lab color space, then flags saturated foreground pixels outside the inclusive safe rectangle `x=48..888, y=288..1248`. It also groups nearby dark connected components into approximate text-line boxes and reports estimates below 40 px. No OCR is used.

## Requirements and run

Install Python 3, OpenCV (`opencv-python`) and NumPy, then run:

```sh
python3 check_safe_area.py video.mp4 --json-out report.json
```

The command prints issue frames and returns `1` if it finds a violation, `0` if none are found, or `2` for an input/read error. JSON includes the coordinates and measurements for issue frames only. Frame numbers start at 0.

## Tuning

For a different pale background, use `--background F4F1E8` (RGB hex, no `#`). Adjust `--background-tolerance` (default 18 in Lab distance) and `--min-saturation` (default 35) for the footage. A lower saturation threshold catches more muted colors; `0` treats all detected foreground as colored. `--dark-threshold`, `--min-component-area`, and `--line-gap` tune the OCR-free dark-text heuristic. Set `--text-roi X1 Y1 X2 Y2` to restrict where text is checked; its end coordinates are exclusive. Safe-rectangle coordinates are inclusive and can be changed with `--safe-rect`.

## Limits

This is a screening heuristic, not OCR or semantic recognition: it cannot tell whether a detected colored pixel is essential, and textured/animated backgrounds or anti-aliased text may need threshold tuning. Text heights are connected-component line-box estimates, not font-size measurements. Review flagged frames and verify the background and thresholds against representative frames before relying on a clean report.
