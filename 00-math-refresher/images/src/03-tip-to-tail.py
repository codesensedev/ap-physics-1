"""Adding two vectors tip-to-tail; the resultant's components are the sums of the components."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from physdraw import Canvas, INK, BLUE, ORANGE, GREY  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "03-tip-to-tail.svg"

A = (4.0, 1.0)
B = (1.5, 3.0)
R = (A[0] + B[0], A[1] + B[1])

c = Canvas(
    720, 400, origin=(70, 340), scale=60,
    title="Vector addition, tip to tail",
    desc="Vector A is drawn first, then vector B starting at the tip of A. The resultant R = A + B runs "
         "from the tail of A to the tip of B. Its components are the sums of the components.",
)
c.grid(0, 6, 0, 5.2, step=1)

tip = (A[0], A[1])
c.arrow((0, 0), A, color=BLUE, width=5, head=15)
c.arrow(tip, R, color=ORANGE, width=5, head=15)
c.arrow((0, 0), R, color=INK, width=5, head=15)

c.text((A[0] / 2, A[1] / 2), "A", italic=True, size=24, color=BLUE, bold=True, dy=34)
c.text((A[0] + B[0] / 2, A[1] + B[1] / 2), "B", italic=True, size=24, color=ORANGE, bold=True, anchor="start", dx=14, dy=6)
c.text((R[0] / 2, R[1] / 2), "R = A + B", italic=True, size=22, color=INK, bold=True, anchor="end", dx=-12, dy=-14)

# component bookkeeping on the right
x0 = 6.15
c.text((x0, 3.6), "Add the components:", size=19, color=GREY, anchor="start", bold=True)
c.text((x0, 2.9), f"R_x = A_x + B_x", size=20, anchor="start")
c.text((x0, 2.45), f"= {A[0]:g} + {B[0]:g} = {R[0]:g}", size=20, anchor="start")
c.text((x0, 1.65), f"R_y = A_y + B_y", size=20, anchor="start")
c.text((x0, 1.2), f"= {A[1]:g} + {B[1]:g} = {R[1]:g}", size=20, anchor="start")

c.save(OUT)
print("   wrote", OUT.name)
