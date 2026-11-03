"""A vector A resolved into its x- and y-components."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from physdraw import Canvas, INK, BLUE, ORANGE, GREEN  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "03-vector-components.svg"

A, THETA = 5.0, 35.0
ax, ay = A * math.cos(math.radians(THETA)), A * math.sin(math.radians(THETA))

c = Canvas(
    660, 420, origin=(90, 350), scale=62,
    title="A vector resolved into components",
    desc="Vector A at angle theta above the x-axis. Its x-component A cos theta lies along the x-axis; "
         "its y-component A sin theta is vertical. Together they form a right triangle with A as hypotenuse.",
)

# axes
c.arrow((-0.4, 0), (8.6, 0), color=INK, width=2, head=11)
c.arrow((0, -0.4), (0, 5.3), color=INK, width=2, head=11)
c.text((8.6, 0), "x", italic=True, size=20, dx=-4, dy=28)
c.text((0, 5.3), "y", italic=True, size=20, dx=-20, dy=8)

# components first, then the vector on top
c.arrow((0, 0), (ax, 0), color=GREEN, width=5, head=15)
c.arrow((ax, 0), (ax, ay), color=ORANGE, width=5, head=15)
c.arrow((0, 0), (ax, ay), color=BLUE, width=5, head=15)

# angle and right-angle marks
c.arc((0, 0), 1.2, 0, THETA, color=INK, width=2)
tx, ty = c.polar((0, 0), 1.65, THETA / 2)
c.text((tx, ty), "θ", italic=True, size=22, dy=7)
c.right_angle((ax, 0), 0.22, 180, 90)

# labels
c.text((ax / 2, ay / 2), "A", italic=True, size=24, color=BLUE, bold=True, dx=-22, dy=-12)
c.text((ax / 2, 0), "A_x = A cos θ", size=20, color=GREEN, bold=True, dy=34)
c.text((ax, ay / 2), "A_y = A sin θ", size=20, color=ORANGE, bold=True, anchor="start", dx=16, dy=6)

c.save(OUT)
print("   wrote", OUT.name)
