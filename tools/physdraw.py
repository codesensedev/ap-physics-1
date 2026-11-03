"""physdraw: a tiny, dependency-free SVG helper for physics diagrams.

Positions are given in *math* coordinates (x to the right, y up) measured in
"units".  The Canvas converts them to pixels:

    scale  = pixels per unit
    origin = pixel position of the math point (0, 0), counted from the
             top-left corner of the image

Text supports simple subscripts:  "A_x",  "v_{x0}".

Every diagram gets a white background so it looks the same in light and dark
GitHub themes.
"""
from __future__ import annotations

import math
import re
from pathlib import Path
from xml.sax.saxutils import escape

# One palette for every image in the course.
INK, BLUE, ORANGE, GREEN, RED = "#1b1f24", "#1f5fbf", "#d9680f", "#23844a", "#c0392b"
GREY, LIGHT, PAPER = "#8a929b", "#e3e7ec", "#ffffff"
FONT = "DejaVu Sans, Helvetica, Arial, sans-serif"

_SUB = re.compile(r"_\{([^}]*)\}|_([A-Za-z0-9])")


def _f(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _rich(s: str):
    """Split 'v_{x0} = 3' into [(text, is_subscript), ...]."""
    parts, pos = [], 0
    for m in _SUB.finditer(s):
        if m.start() > pos:
            parts.append((s[pos:m.start()], False))
        parts.append((m.group(1) if m.group(1) is not None else m.group(2), True))
        pos = m.end()
    if pos < len(s):
        parts.append((s[pos:], False))
    return parts


def _tspans(s: str, size: float) -> str:
    """Build <tspan>s.  Spaces at the start/end of a segment are turned into an
    explicit dx offset, because renderers disagree about whitespace next to a
    subscript."""
    out, cur = [], 0.0
    parts = _rich(s)
    for i, (txt, sub) in enumerate(parts):
        want = size * 0.28 if sub else 0.0
        fs = f' font-size="{_f(size * 0.72)}"' if sub else ""
        lead = len(txt) - len(txt.lstrip(" "))
        txt = txt.lstrip(" ")
        dx = f' dx="{_f(lead * size * 0.32)}"' if lead and i > 0 else ""
        if lead and i == 0:
            txt = " " * lead + txt
        # the gap before the *next* segment was already moved into its own dx
        trail = len(txt) - len(txt.rstrip(" "))
        if trail and i < len(parts) - 1:
            txt = txt.rstrip(" ")
            parts[i + 1] = (" " * trail + parts[i + 1][0], parts[i + 1][1])
        txt = txt.replace(" ", " ")
        out.append(f'<tspan{dx} dy="{_f(want - cur)}"{fs}>{escape(txt)}</tspan>')
        cur = want
    return "".join(out)


class Canvas:
    def __init__(self, width, height, *, origin=(0, 0), scale=40, title="", desc=""):
        self.w, self.h = width, height
        self.ox, self.oy = origin
        self.k = scale
        self.title, self.desc = title, desc
        self._items: list[str] = []

    # ---- coordinate helpers -------------------------------------------------
    def px(self, x, y):
        return self.ox + self.k * x, self.oy - self.k * y

    @staticmethod
    def polar(center, r, deg):
        a = math.radians(deg)
        return center[0] + r * math.cos(a), center[1] + r * math.sin(a)

    # ---- primitives ---------------------------------------------------------
    def line(self, p, q, color=INK, width=2, dash=None):
        (x1, y1), (x2, y2) = self.px(*p), self.px(*q)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self._items.append(
            f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"{d}/>'
        )

    def arrow(self, p, q, color=BLUE, width=3, head=13, dash=None):
        (x1, y1), (x2, y2) = self.px(*p), self.px(*q)
        ang = math.atan2(y2 - y1, x2 - x1)
        length = math.hypot(x2 - x1, y2 - y1)
        h = min(head, length * 0.6)
        ca, sa = math.cos(ang), math.sin(ang)
        bx, by = x2 - 0.85 * h * ca, y2 - 0.85 * h * sa
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self._items.append(
            f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(bx)}" y2="{_f(by)}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="butt"{d}/>'
        )
        cx, cy = x2 - h * ca, y2 - h * sa
        wx, wy = -sa * 0.42 * h, ca * 0.42 * h
        pts = f"{_f(x2)},{_f(y2)} {_f(cx + wx)},{_f(cy + wy)} {_f(cx - wx)},{_f(cy - wy)}"
        self._items.append(f'<polygon points="{pts}" fill="{color}"/>')

    def polyline(self, pts, color=INK, width=2, dash=None):
        s = " ".join(f"{_f(x)},{_f(y)}" for x, y in (self.px(*p) for p in pts))
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self._items.append(
            f'<polyline points="{s}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round"{d}/>'
        )

    def rect(self, x, y, w, h, fill=LIGHT, stroke=INK, sw=2):
        left, top = self.px(x, y + h)
        self._items.append(
            f'<rect x="{_f(left)}" y="{_f(top)}" width="{_f(w * self.k)}" height="{_f(h * self.k)}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def circle(self, c, r_px=6, fill=INK, stroke="none", sw=0):
        x, y = self.px(*c)
        self._items.append(
            f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r_px)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def arc(self, c, r, a0, a1, color=INK, width=2):
        """Counter-clockwise arc of radius r (units) from angle a0 to a1 (degrees)."""
        sx, sy = self.px(*self.polar(c, r, a0))
        ex, ey = self.px(*self.polar(c, r, a1))
        R = r * self.k
        large = 1 if abs(a1 - a0) > 180 else 0
        self._items.append(
            f'<path d="M {_f(sx)} {_f(sy)} A {_f(R)} {_f(R)} 0 {large} 0 {_f(ex)} {_f(ey)}" '
            f'fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
        )

    def right_angle(self, corner, size, a1, a2, color=INK, width=1.8):
        p1 = self.polar(corner, size, a1)
        p3 = self.polar(corner, size, a2)
        p2 = (p1[0] + p3[0] - corner[0], p1[1] + p3[1] - corner[1])
        self.polyline([p1, p2, p3], color=color, width=width)

    def grid(self, xmin, xmax, ymin, ymax, step=1, color=LIGHT):
        x = xmin
        while x <= xmax + 1e-9:
            self.line((x, ymin), (x, ymax), color=color, width=1)
            x += step
        y = ymin
        while y <= ymax + 1e-9:
            self.line((xmin, y), (xmax, y), color=color, width=1)
            y += step

    def text(self, p, s, size=18, color=INK, anchor="middle", italic=False, bold=False, dx=0, dy=0):
        x, y = self.px(*p)
        style = (' font-style="italic"' if italic else "") + (' font-weight="bold"' if bold else "")
        self._items.append(
            f'<text x="{_f(x + dx)}" y="{_f(y + dy)}" font-family="{FONT}" font-size="{size}" '
            f'fill="{color}" text-anchor="{anchor}"{style}>{_tspans(s, size)}</text>'
        )

    # ---- output -------------------------------------------------------------
    def save(self, path):
        body = "\n".join(self._items)
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-labelledby="t d">\n'
            f'<title id="t">{escape(self.title)}</title>\n<desc id="d">{escape(self.desc)}</desc>\n'
            f'<rect width="100%" height="100%" fill="{PAPER}"/>\n{body}\n</svg>\n'
        )
        Path(path).write_text(svg, encoding="utf-8")
