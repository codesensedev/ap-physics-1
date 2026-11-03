"""Regenerate every image in the course:

    python tools/build_images.py

Each image has a small script in <unit>/images/src/ that writes the SVG one
folder up.  Edit the script, run this, commit both.
"""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for script in sorted(root.glob("*/images/src/*.py")):
    print("->", script.relative_to(root))
    subprocess.run([sys.executable, str(script)], check=True)
