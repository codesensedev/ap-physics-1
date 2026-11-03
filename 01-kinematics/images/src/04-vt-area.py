"""Area under a v-t line = displacement.  Splitting the trapezoid gives x = v0*t + 1/2*a*t^2."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import plotstyle as ps  # noqa: E402

ps.setup()
OUT = Path(__file__).resolve().parents[1] / "04-vt-area.svg"

v0, a, T = 3.0, 2.0, 4.0
vf = v0 + a * T
rect, tri = v0 * T, 0.5 * (a * T) * T

fig, ax = plt.subplots(figsize=(6.6, 4.6))
t = np.linspace(0, T, 100)
ax.fill_between([0, T], [0, 0], [v0, v0], color=ps.ORANGE, alpha=0.30, lw=0)
ax.fill([0, T, T], [v0, vf, v0], color=ps.BLUE, alpha=0.25, lw=0)
ax.plot(t, v0 + a * t, color=ps.BLUE)

ax.text(T / 2, v0 / 2, f"rectangle\n$v_0\\,t = {v0:g}\\times{T:g} = {rect:g}$ m",
        ha="center", va="center", color=ps.ORANGE, fontweight="bold", fontsize=11.5)
ax.text(3.0, 5.0, f"triangle\n$\\frac{{1}}{{2}}(at)(t) = \\frac{{1}}{{2}}at^2$\n$= \\frac{{1}}{{2}}({a:g})({T:g}^2) = {tri:g}$ m",
        ha="center", va="center", color=ps.BLUE, fontweight="bold", fontsize=11.5)
ax.text(0.15, 10.2, f"Δx = {rect:g} + {tri:g} = {rect + tri:g} m", color=ps.INK, fontweight="bold", fontsize=13)

ax.set(xlim=(0, 4.5), ylim=(0, 12), xlabel="t  (s)", ylabel="v  (m/s)",
       title="Area under the v–t line = displacement")
ax.set_xticks([0, T], ["0", f"t = {T:g}"])
ax.set_yticks([0, v0, vf], ["0", f"$v_0 = {v0:g}$", f"$v = {vf:g}$"])

fig.tight_layout()
ps.save(fig, OUT)
print("   wrote", OUT.name)
