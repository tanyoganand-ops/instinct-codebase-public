# v9 Branch 2 (MATERIAL) build notes
File: claude-vs-gemini-v9-material.mp4 - 1080x1920, 30 fps, 450 frames (15.000 s), H.264 yuv420p, silent.
Script: v9-material-build.py (numpy/PIL/scipy, per-frame render, no AI video).

Content (exact): Sonnet 5.5 (Max) vs Gemini 4 (Argon High). Terminal-Bench 4.0 64/57. AutomationBench-AA 71/78. "Different tests. Different winners." CTA "COMMENT VIDEO". Rail "Artificial Analysis - 30 Sep 2026" / "Sonnet Max / Argon High". Bar length = value/100 of the groove.
Added copy not in brief: "SONNET/GEMINI LEADS HERE", "WANT MORE LIKE THIS?" (B6 line, swap if unwanted), verdict card rows "Terminal-Bench: Sonnet 5.5" / "AutomationBench: Gemini 4". "Argon: limited rollout" caveat is NOT in the rail (no room at 48px).

Material: porcelain/clay tiles from a rounded-rect SDF: bevel height -> normals -> diffuse + spec + edge rim, subsurface tint near edges (peach for Claude, periwinkle for Gemini), AO, two-layer contact+soft shadow whose offset follows the light. One light moves per beat (top-left, top-centre, left, right, top, centre) and drives shading, shadow offset and a faint bg glow. Specular sweeps on tile entry and when each leader's bar lands (enamel glint). Winner tile gets higher elevation (bigger shadow).
Glass = accent only: logo lenses (convex refraction, per-channel dispersion, fresnel/specular rim) and frosted plates for the hook and verdict (edge refraction, rim light, sweep). Everything else is solid porcelain. Lacquered navy CTA with a press at ~f402.
Background pale (#F5F4F2 + faint pastel drift, 1% silk bands, grain dither). Motion: drop-down / left-right swipes, eased, no fly/spin/zoom, no hard cuts, 14-16 frame handoffs.
Legibility: rail 48px Inter 600, benchmark names 56px Inter 800, verdict 96px Anton, CTA 84px Anton, supporting 48px. All content inside safe rect x48-888, y288-1248 (rail bottom = 1248).

Sources/attribution: Anton (SIL OFL, Google Fonts), Inter (SIL OFL). Logos: Simple Icons (CC0) anthropic.svg and googlegemini.svg; Anthropic mark path is parsed as polygons from the supplied SVG, the Gemini star is a superellipse approximation of the supplied mark (not the exact path, colour #8E75B2 kept). Trademarks belong to Anthropic and Google. Layout/timing spine: v9-branch-composition-plans plan 2; clay token palette feel from the supplied Clay reference tokens (not copied). Scores per main's AA launch-article verification (not re-checked by me).
Checked: contact-sheet frames at f10/50/92/174/262/356/408/449 inspected; ffprobe 15.000 s, 450 frames.
