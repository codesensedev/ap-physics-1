"""Motion diagram: an object speeding up from rest with constant acceleration.

Dots are the object's position at equal time intervals (1 s).  Blue arrows are
the velocity at each instant (length proportional to speed); the green arrow is
the (constant) acceleration.  Here x = t^2 (a = 2 units/s^2), v = 2t.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from physdraw import Canvas, INK, BLUE, GREEN, GREY, LIGHT  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "04-motion-diagram.svg"

c = Canvas(
    820, 260, origin=(50, 140), scale=40,
    title="Motion diagram for constant acceleration",
    desc="Five dots show an object's position every second while it speeds up from rest. The gaps between "
         "dots grow, the velocity arrows get longer by the same amount each step, and the acceleration "
         "arrow points the same way as the motion.",
)

c.text((8.2, 2.9), "Dots show position at equal time steps (every 1 s)", size=18, color=GREY, bold=True)
c.line((-0.5, 0), (17.2, 0), color=LIGHT, width=3)

VSCALE = 0.32  # arrow length (units) per unit of velocity
for t in range(5):
    x, v = t**2, 2 * t
    c.circle((x, 0), 7, fill=INK)
    c.text((x, 0), f"{t} s", size=16, color=GREY, dy=34)
    if v:
        c.arrow((x, 0.9), (x + VSCALE * v, 0.9), color=BLUE, width=4, head=12)
    else:
        c.text((x, 0.9), "v = 0", size=16, color=BLUE, bold=True, dy=-4)
c.text((16 + VSCALE * 8 / 2, 0.9), "v", italic=True, size=22, color=BLUE, bold=True, dy=-14)

c.arrow((0, -1.95), (2.4, -1.95), color=GREEN, width=5, head=15)
c.text((2.8, -1.95), "a: constant, same direction as v  →  speeding up",
       size=18, color=GREEN, bold=True, anchor="start", dy=6)

c.save(OUT)
print("   wrote", OUT.name)
