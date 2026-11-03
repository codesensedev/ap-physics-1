"""Graph for practice problem 5 of lesson 04 (no answers drawn on it)."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import plotstyle as ps  # noqa: E402

ps.setup()
OUT = Path(__file__).resolve().parents[1] / "04-practice-vt-graph.svg"

pts_t = [0, 4, 8, 10]
pts_v = [0, 8, 8, 0]

fig, ax = plt.subplots(figsize=(6.6, 3.8))
ax.plot(pts_t, pts_v, color=ps.BLUE)
ax.set(xlim=(0, 11), ylim=(0, 10), xlabel="t  (s)", ylabel="v  (m/s)", title="Problem 5: velocity of a cart")
ax.set_xticks(range(0, 12))
ax.set_yticks(range(0, 11, 2))

fig.tight_layout()
ps.save(fig, OUT)
print("   wrote", OUT.name)
