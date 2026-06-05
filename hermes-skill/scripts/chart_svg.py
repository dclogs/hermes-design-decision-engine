#!/usr/bin/env python3
"""
SVG chart generator for self-contained HTML proposals.
Zero external dependencies — pure Python SVG generation.
Supports: bar, line, donut, radar

Usage:
  python3 chart_svg.py bar --data '["A",85,"B",72,"C",93]' --width 400 --height 300
  python3 chart_svg.py line --data '[["1月",40],["2月",55],["3月",70]]'
  python3 chart_svg.py donut --data '["A",45,"B",30,"C",25]'
  python3 chart_svg.py radar --data '["S1",90,"S2",75,"S3",82]'
  python3 chart_svg.py bar --data '["A",85,"B",72]' --palette "#E65100,#10B981,#6B7280"

Input format: JSON flat array of label,value pairs, or nested for line.
Output: SVG string to stdout.
"""

import json
import math
import sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape


def esc(text):
    return escape(str(text))


def parse_data(raw):
    """Parse flat JSON array into list of (label, value) tuples."""
    arr = json.loads(raw)
    if isinstance(arr[0], list):
        # Multiple series for line charts
        return arr
    result = []
    for i in range(0, len(arr), 2):
        result.append((str(arr[i]), float(arr[i + 1])))
    return result


def svg_tag(name, attrs=None, content=None):
    """Build an SVG element string."""
    attrs = attrs or {}
    parts = [f"<{name}"]
    for k, v in attrs.items():
        parts.append(f' {k}="{esc(str(v))}"')
    if content is None:
        parts.append(" />")
    else:
        parts.append(f">{content}</{name}>")
    return "".join(parts)


def svg_wrapper(content, width, height, view_box=None):
    vb = view_box or f"0 0 {width} {height}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" viewBox="{vb}" '
        f'style="font-family:\'Noto Sans SC\',\'Inter\',sans-serif;font-size:12px;color:#374151;">'
        f'\n{content}\n</svg>'
    )


# ─── Default palette (IBM Carbon / Open Color inspired) ──────────────────────
# Override with --palette "color1,color2,color3,..."
DEFAULT_COLORS = ["#3B82F6", "#10B981", "#F59E0B", "#EF4444",
                  "#8B5CF6", "#EC4899", "#14B8A6", "#F97316"]
DEFAULT_COLORS_LIGHT = ["#DBEAFE", "#D1FAE5", "#FEF3C7", "#FEE2E2",
                        "#EDE9FE", "#FCE7F3", "#CCFBF1", "#FFEDD5"]
BLUE = "#3B82F6"
GRAY = "#6B7280"
GRAY_LIGHT = "#E5E7EB"
WHITE = "#FFFFFF"


def resolve_palette(palette_str):
    """Parse --palette arg into COLORS and COLORS_LIGHT lists."""
    if not palette_str:
        return DEFAULT_COLORS, DEFAULT_COLORS_LIGHT
    colors = [c.strip() for c in palette_str.split(",") if c.strip()]
    # Generate light variants (opacity approach)
    lights = []
    for c in colors:
        # Simple lightening: prepend the hex
        lights.append(c)
    return colors, lights


# ─── Chart generators ────────────────────────────────────────────────────────

def generate_bar(data, width, height, palette=None, horizontal=False):
    """Vertical bar chart."""
    if not data:
        return ""
    COLORS, _ = resolve_palette(palette)

    labels = [d[0] for d in data]
    values = [d[1] for d in data]
    max_val = max(values) if values else 1

    padding = {"top": 30, "right": 20, "bottom": 50, "left": 50}
    chart_w = width - padding["left"] - padding["right"]
    chart_h = height - padding["top"] - padding["bottom"]

    n = len(data)
    bar_gap = chart_w * 0.1
    bar_total = chart_w - bar_gap
    bar_width = max(8, bar_total / n - bar_gap / n)

    elements = []

    # Y-axis grid lines and labels
    num_grid = 4
    for i in range(num_grid + 1):
        y = padding["top"] + chart_h - (chart_h * i / num_grid)
        val = max_val * i / num_grid
        elements.append(
            svg_tag("line", {
                "x1": padding["left"], "y1": f"{y:.1f}",
                "x2": width - padding["right"], "y2": f"{y:.1f}",
                "stroke": GRAY_LIGHT, "stroke-width": "1"
            })
        )
        elements.append(
            svg_tag("text", {
                "x": padding["left"] - 8, "y": y + 4,
                "text-anchor": "end", "fill": GRAY
            }, f"{val:.0f}")
        )

    # Bars
    for i, (label, value) in enumerate(data):
        x = padding["left"] + bar_gap / 2 + i * (bar_width + bar_gap / n)
        bar_h = max(1, chart_h * value / max_val)
        y = padding["top"] + chart_h - bar_h
        color = COLORS[i % len(COLORS)]

        elements.append(
            svg_tag("rect", {
                "x": f"{x:.1f}", "y": f"{y:.1f}",
                "width": f"{bar_width:.1f}", "height": f"{bar_h:.1f}",
                "fill": color, "rx": "2", "ry": "2"
            })
        )

        # Value label on top
        elements.append(
            svg_tag("text", {
                "x": f"{x + bar_width / 2:.1f}", "y": y - 6,
                "text-anchor": "middle", "fill": GRAY,
                "font-size": "11px", "font-weight": "600"
            }, f"{value:.0f}")
        )

        # Label below
        elements.append(
            svg_tag("text", {
                "x": f"{x + bar_width / 2:.1f}",
                "y": padding["top"] + chart_h + 16,
                "text-anchor": "end" if n > 4 else "middle",
                "fill": GRAY, "font-size": "11px",
                "transform": f"rotate(-30,{x + bar_width / 2:.1f},{padding['top'] + chart_h + 16})"
                if n > 4 else ""
            }, label[:12])
        )

    return svg_wrapper("\n".join(elements), width, height)


def generate_line(data, width, height, palette=None):
    """Line chart. data is flat list of (label, value) tuples or list of these for multi-series."""
    if not data:
        return ""
    COLORS, _ = resolve_palette(palette)

    # If data[0] is a list/tuple but its first element is not a list/tuple,
    # it's single-series format [[label,val],[label,val]]
    if data and isinstance(data[0], (list, tuple)) and not isinstance(data[0][0], (list, tuple)):
        series_list = [data]
    else:
        series_list = data

    padding = {"top": 30, "right": 20, "bottom": 50, "left": 50}
    chart_w = width - padding["left"] - padding["right"]
    chart_h = height - padding["top"] - padding["bottom"]

    elements = []

    # Collect all values
    all_vals = []
    labels = []
    for series in series_list:
        for item in series:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                all_vals.append(float(item[1]))
                labels.append(str(item[0]))

    if not all_vals:
        return ""
    max_val = max(all_vals) if all_vals else 1
    min_val = min(min(all_vals), 0)
    val_range = max_val - min_val if max_val != min_val else 1

    # Grid lines
    num_grid = 4
    for i in range(num_grid + 1):
        y = padding["top"] + chart_h - (chart_h * i / num_grid)
        val = min_val + val_range * i / num_grid
        elements.append(
            svg_tag("line", {
                "x1": padding["left"], "y1": f"{y:.1f}",
                "x2": width - padding["right"], "y2": f"{y:.1f}",
                "stroke": GRAY_LIGHT, "stroke-width": "1"
            })
        )
        elements.append(
            svg_tag("text", {
                "x": padding["left"] - 8, "y": y + 4,
                "text-anchor": "end", "fill": GRAY
            }, f"{val:.0f}")
        )

    # Each series
    for si, series in enumerate(series_list):
        color = COLORS[si % len(COLORS)]
        points = []
        n = len(series)

        for i, item in enumerate(series):
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                val = float(item[1])
                x = padding["left"] + (chart_w * i / (n - 1)) if n > 1 else padding["left"] + chart_w / 2
                y = padding["top"] + chart_h - (chart_h * (val - min_val) / val_range)
                points.append(f"{x:.1f},{y:.1f}")

        if len(points) >= 2:
            # Line
            elements.append(
                svg_tag("polyline", {
                    "points": " ".join(points),
                    "fill": "none", "stroke": color,
                    "stroke-width": "2", "stroke-linejoin": "round"
                })
            )
            # Dots
            for pi, pt in enumerate(points):
                cx, cy = pt.split(",")
                elements.append(
                    svg_tag("circle", {
                        "cx": cx, "cy": cy, "r": "3.5",
                        "fill": color, "stroke": WHITE, "stroke-width": "1.5"
                    })
                )
                if si == 0:
                    val = series[pi][1]
                    elements.append(
                        svg_tag("text", {
                            "x": cx, "y": str(float(cy) - 10),
                            "text-anchor": "middle",
                            "fill": GRAY, "font-size": "11px",
                            "font-weight": "600"
                        }, f"{val:.0f}")
                    )

        # X labels (first series)
        if si == 0:
            for i, item in enumerate(series):
                if isinstance(item, (list, tuple)):
                    x = padding["left"] + (chart_w * i / (n - 1)) if n > 1 else padding["left"] + chart_w / 2
                    elements.append(
                        svg_tag("text", {
                            "x": f"{x:.1f}",
                            "y": padding["top"] + chart_h + 16,
                            "text-anchor": "end" if n > 4 else "middle",
                            "fill": GRAY, "font-size": "11px",
                            "transform": f"rotate(-20,{x:.1f},{padding['top'] + chart_h + 16})"
                            if n > 6 else ""
                        }, str(item[0])[:12])
                    )

    return svg_wrapper("\n".join(elements), width, height)


def generate_donut(data, width, height, palette=None):
    """Donut/pie chart."""
    if not data:
        return ""
    COLORS, _ = resolve_palette(palette)

    total = sum(d[1] for d in data)
    if total == 0:
        return ""

    cx = width / 2
    cy = height / 2
    outer_r = min(width, height) * 0.38
    inner_r = outer_r * 0.6

    elements = []
    current_angle = -90

    for i, (label, value) in enumerate(data):
        ratio = value / total
        angle = 360 * ratio
        end_angle = current_angle + angle
        color = COLORS[i % len(COLORS)]

        start_rad = math.radians(current_angle)
        end_rad = math.radians(end_angle)

        x1 = cx + outer_r * math.cos(start_rad)
        y1 = cy + outer_r * math.sin(start_rad)
        x2 = cx + outer_r * math.cos(end_rad)
        y2 = cy + outer_r * math.sin(end_rad)

        x1_in = cx + inner_r * math.cos(end_rad)
        y1_in = cy + inner_r * math.sin(end_rad)
        x2_in = cx + inner_r * math.cos(start_rad)
        y2_in = cy + inner_r * math.sin(start_rad)

        large_arc = 1 if angle > 180 else 0

        path = (
            f"M {x1:.1f} {y1:.1f} "
            f"A {outer_r} {outer_r} 0 {large_arc} 1 {x2:.1f} {y2:.1f} "
            f"L {x1_in:.1f} {y1_in:.1f} "
            f"A {inner_r} {inner_r} 0 {large_arc} 0 {x2_in:.1f} {y2_in:.1f} Z"
        )

        elements.append(
            svg_tag("path", {
                "d": path, "fill": color
            })
        )

        # Label and percentage outside
        label_angle = current_angle + angle / 2
        label_rad = math.radians(label_angle)
        label_r = outer_r + 22
        lx = cx + label_r * math.cos(label_rad)
        ly = cy + label_r * math.sin(label_rad)

        pct = ratio * 100
        short_label = label[:8]
        if pct >= 5:
            elements.append(
                svg_tag("text", {
                    "x": f"{lx:.1f}", "y": f"{ly:.1f}",
                    "text-anchor": "middle", "fill": GRAY,
                    "font-size": "10px", "font-weight": "500"
                }, f"{short_label} {pct:.0f}%")
            )

        current_angle = end_angle

    # Center total
    elements.append(
        svg_tag("text", {
            "x": f"{cx:.1f}", "y": f"{cy + 5:.1f}",
            "text-anchor": "middle", "fill": "#374151",
            "font-size": "18px", "font-weight": "700"
        }, f"{total:.0f}")
    )

    return svg_wrapper("\n".join(elements), width, height)


def generate_radar(data, width, height, palette=None):
    """Radar chart for multi-dimension comparison."""
    if not data:
        return ""
    if len(data) < 3:
        return ""
    COLORS, _ = resolve_palette(palette)

    cx = width / 2
    cy = height / 2
    radius = min(width, height) * 0.35

    values = [d[1] for d in data]
    labels = [d[0] for d in data]
    max_val = max(values) if values else 1

    elements = []

    # Background grid
    for level in range(1, 5):
        r = radius * level / 4
        points = []
        for i in range(len(data)):
            angle = 2 * math.pi * i / len(data) - math.pi / 2
            px = cx + r * math.cos(angle)
            py = cy + r * math.sin(angle)
            points.append(f"{px:.1f},{py:.1f}")
        elements.append(
            svg_tag("polygon", {
                "points": " ".join(points),
                "fill": "none", "stroke": GRAY_LIGHT, "stroke-width": "1"
            })
        )

    # Axis lines
    for i in range(len(data)):
        angle = 2 * math.pi * i / len(data) - math.pi / 2
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        elements.append(
            svg_tag("line", {
                "x1": f"{cx:.1f}", "y1": f"{cy:.1f}",
                "x2": f"{px:.1f}", "y2": f"{py:.1f}",
                "stroke": GRAY_LIGHT, "stroke-width": "1"
            })
        )

    # Data polygon
    color = COLORS[0]
    points = []
    for i, (label, value) in enumerate(data):
        ratio = value / max_val
        angle = 2 * math.pi * i / len(data) - math.pi / 2
        px = cx + radius * ratio * math.cos(angle)
        py = cy + radius * ratio * math.sin(angle)
        points.append(f"{px:.1f},{py:.1f}")

    elements.append(
        svg_tag("polygon", {
            "points": " ".join(points),
            "fill": color, "fill-opacity": "0.15",
            "stroke": color, "stroke-width": "2"
        })
    )

    # Data dots
    for i, (label, value) in enumerate(data):
        ratio = value / max_val
        angle = 2 * math.pi * i / len(data) - math.pi / 2
        px = cx + radius * ratio * math.cos(angle)
        py = cy + radius * ratio * math.sin(angle)
        elements.append(
            svg_tag("circle", {
                "cx": f"{px:.1f}", "cy": f"{py:.1f}",
                "r": "3.5", "fill": color, "stroke": WHITE, "stroke-width": "1.5"
            })
        )

    # Labels
    for i, (label, value) in enumerate(data):
        angle = 2 * math.pi * i / len(data) - math.pi / 2
        lx = cx + (radius + 24) * math.cos(angle)
        ly = cy + (radius + 24) * math.sin(angle)
        anchor = "middle"
        if abs(math.cos(angle)) < 0.1:
            anchor = "middle"
        elif math.cos(angle) > 0:
            anchor = "start"
        else:
            anchor = "end"
        elements.append(
            svg_tag("text", {
                "x": f"{lx:.1f}", "y": f"{ly + 4:.1f}",
                "text-anchor": anchor, "fill": GRAY,
                "font-size": "11px", "font-weight": "500"
            }, f"{label} {value:.0f}")
        )

    return svg_wrapper("\n".join(elements), width, height)


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: chart_svg.py <bar|line|donut|radar> [--data JSON] [--width N] [--height N] [--palette #c1,#c2,...]",
              file=sys.stderr)
        sys.exit(1)

    chart_type = sys.argv[1]
    raw_data = None
    width, height = 400, 280
    palette = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--data" and i + 1 < len(sys.argv):
            raw_data = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--width" and i + 1 < len(sys.argv):
            width = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--height" and i + 1 < len(sys.argv):
            height = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--palette" and i + 1 < len(sys.argv):
            palette = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    if not raw_data:
        raw_data = sys.stdin.read().strip()

    parsed = parse_data(raw_data)

    generators = {
        "bar": generate_bar,
        "line": generate_line,
        "donut": generate_donut,
        "radar": generate_radar,
    }

    if chart_type not in generators:
        print(f"Unknown chart type: {chart_type}", file=sys.stderr)
        print(f"Supported: {', '.join(generators.keys())}", file=sys.stderr)
        sys.exit(1)

    svg = generators[chart_type](parsed, width, height, palette=palette)
    print(svg)


if __name__ == "__main__":
    main()
