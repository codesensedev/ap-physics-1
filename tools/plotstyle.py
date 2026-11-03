"""Shared matplotlib style so every generated graph looks like part of one course."""
import matplotlib as mpl

BLUE, ORANGE, GREEN, INK, GREY = "#1f5fbf", "#d9680f", "#23844a", "#1b1f24", "#8a929b"


def setup():
    mpl.use("Agg")
    mpl.rcParams.update(
        {
            "svg.fonttype": "path",          # text becomes outlines: renders identically everywhere
            "svg.hashsalt": "ap-physics-1",  # deterministic ids -> clean git diffs
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "font.size": 12,
            "axes.titlesize": 13,
            "axes.titleweight": "bold",
            "axes.labelsize": 12,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": INK,
            "axes.labelcolor": INK,
            "axes.grid": True,
            "grid.color": "#e3e7ec",
            "grid.linewidth": 0.8,
            "text.color": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "lines.linewidth": 2.5,
            "mathtext.default": "it",
        }
    )


def save(fig, path):
    fig.savefig(path, format="svg", metadata={"Date": None}, bbox_inches="tight")
