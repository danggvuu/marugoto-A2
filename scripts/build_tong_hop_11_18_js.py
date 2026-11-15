"""Validate the hand-maintained exam controller; never overwrite it with a stale copy.

The canonical source is assets/js/pages/de_thi_tong_hop_11_18.js.
Kept as a build entry point for existing workflows.
"""
from pathlib import Path
import subprocess

controller = Path(__file__).resolve().parents[1] / "assets/js/pages/de_thi_tong_hop_11_18.js"
subprocess.run(["node", "--check", str(controller)], check=True)
print(f"Validated canonical controller: {controller.name}")
