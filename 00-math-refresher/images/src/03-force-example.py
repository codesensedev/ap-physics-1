"""Worked example: a 50 N pull at 30 degrees above the horizontal, split into components."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from physdraw import Canvas, INK, BLUE, ORANGE, GREEN, LIGHT  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "03-force-example.svg"

F, TH = 50.0, 30.0
fx, fy = F * math.cos(math.radians(TH)), F * math.sin(math.radians(TH))

L = 5.0  # drawn length of the arrow in units (not to scale with 50 N)
dx, dy = L * math.cos(math.radians(TH)), L * math.sin(math.radians(TH))
P = (4.4, 0.8)          # where the rope is attached
tip = (P[0] + dx, P[1] + dy)

c = Canvas(
    700, 330, origin=(60, 275), scale=56,
    title="A 50 newton pull at 30 degrees above horizontal",
    desc=f"A box on the floor is pulled by a rope with force 50 N at 30 degrees above the horizontal. "
         f"The horizontal component is {fx:.1f} N and the vertical component is {fy:.1f} N.",
)

c.line((0, 0), (11.4, 0), color=INK, width=3)                      # floor
c.rect(1.8, 0, 2.6, 1.4, fill=LIGHT, stroke=INK, sw=2.5)           # box
c.text((3.1, 0.7), "box", size=20, dy=7)

# components (dashed), then the force
c.arrow(P, (tip[0], P[1]), color=GREEN, width=4, head=14, dash="8 6")
c.arrow((tip[0], P[1]), tip, color=ORANGE, width=4, head=14, dash="8 6")
c.arrow(P, tip, color=BLUE, width=5, head=15)
c.right_angle((tip[0], P[1]), 0.22, 180, 90)

# angle
c.arc(P, 1.5, 0, TH, color=INK, width=2)
ax_, ay_ = c.polar(P, 2.05, TH / 2)
c.text((ax_, ay_), f"{TH:g}°", size=19, dy=6)

# labels
c.text((P[0] + dx / 2, P[1] + dy / 2), f"F = {F:g} N", italic=True, size=22, color=BLUE, bold=True,
       anchor="end", dx=-10, dy=-12)
c.text((P[0] + dx / 2, P[1]), f"F_x = {fx:.1f} N", size=20, color=GREEN, bold=True, dy=30)
c.text((tip[0], P[1] + dy / 2), f"F_y = {fy:.1f} N", size=20, color=ORANGE, bold=True, anchor="start", dx=14, dy=6)

c.save(OUT)
print("   wrote", OUT.name)
