"""The three linked graphs for constant acceleration: a-t, v-t and x-t."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import plotstyle as ps  # noqa: E402

ps.setup()
OUT = Path(__file__).resolve().parents[1] / "04-graphs-constant-a.svg"

x0, v0, a = 0.0, 2.0, 1.5          # m, m/s, m/s^2
t = np.linspace(0, 4, 200)
v = v0 + a * t
x = x0 + v0 * t + 0.5 * a * t**2

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6.6, 8.6), sharex=True)

# --- a-t --------------------------------------------------------------------
ax1.plot(t, np.full_like(t, a), color=ps.GREEN)
ax1.set(ylim=(0, 3), ylabel="a  (m/s²)", title="Acceleration is constant")
ax1.text(2, a + 0.35, "a = 1.5 m/s²  (a flat line)", ha="center", color=ps.GREEN, fontweight="bold")

# --- v-t --------------------------------------------------------------------
ax2.plot(t, v, color=ps.BLUE)
ax2.set(ylim=(0, 9), ylabel="v  (m/s)", title="Velocity changes at a steady rate: slope = a")
t1, t2 = 1.0, 3.0
v1, v2 = v0 + a * t1, v0 + a * t2
ax2.plot([t1, t2], [v1, v1], "--", color=ps.GREY, lw=1.5)
ax2.plot([t2, t2], [v1, v2], "--", color=ps.GREY, lw=1.5)
ax2.text((t1 + t2) / 2, v1 - 0.75, "Δt = 2 s", ha="center", color=ps.GREY)
ax2.text(t2 + 0.1, (v1 + v2) / 2, f"Δv = {v2 - v1:g} m/s", va="center", color=ps.GREY)
ax2.text(0.15, 7.6, f"slope = Δv/Δt = {(v2 - v1) / (t2 - t1):g} m/s² = a", color=ps.BLUE, fontweight="bold")

# --- x-t --------------------------------------------------------------------
ax3.plot(t, x, color=ps.INK)
ax3.set(ylim=(0, 22), xlabel="t  (s)", ylabel="x  (m)", title="Position curves upward: slope = velocity")
for t0, color in ((1.0, ps.ORANGE), (3.0, ps.ORANGE)):
    xt, vt = x0 + v0 * t0 + 0.5 * a * t0**2, v0 + a * t0
    tt = np.array([t0 - 0.8, t0 + 0.8])
    ax3.plot(tt, xt + vt * (tt - t0), color=color, lw=2)
    ax3.plot([t0], [xt], "o", color=color)
    ax3.annotate(f"slope = {vt:g} m/s", (t0 + 0.8, xt + vt * 0.8), xytext=(8, -14),
                 textcoords="offset points", color=color, fontweight="bold")
ax3.set_xlim(0, 4.6)

fig.tight_layout()
ps.save(fig, OUT)
print("   wrote", OUT.name)
