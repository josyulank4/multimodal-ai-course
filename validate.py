"""End-to-end validation for the Course 7 code repository.
Runs every lesson demo as a subprocess (exactly how a student runs them)
and checks expected output markers. Run from the repo root: python validate.py
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent
FAILURES = []
COUNT = [0]
def check(name, condition, detail=""):
    COUNT[0] += 1
    print(f"[{'PASS' if condition else 'FAIL'}] {name}" + (f" — {detail}" if detail and not condition else ""))
    if not condition: FAILURES.append(name)
def expect(module, markers):
    proc = subprocess.run([sys.executable, "-m", module], cwd=REPO_ROOT, capture_output=True, text=True, timeout=120)
    check(f"{module}: runs end-to-end (exit 0)", proc.returncode == 0, proc.stderr.strip()[-300:])
    for m in markers: check(f"{module}: output contains {m!r}", m in proc.stdout)
def main():
    print("== module demos (subprocess) ==")
    expect("visiontriage.cascade", ["cascade: 3/6 auto-decided, 2 escalated to vlm, 1 to human", "visiontriage demo complete"])
    expect("voiceloop.budget", ["voice loop total: 1180 ms of 1200 ms budget", "verdict: WITHIN BUDGET", "voiceloop demo complete"])
    expect("docintel.extract", ["reconciliation:", "MATCH", "docintel demo complete"])
    expect("crossmodal.search", ["top hit: photo:red-jacket", "crossmodal demo complete"])
    expect("fusiongate.fuse", ["gate: ESCALATE", "fusiongate demo complete"])
    expect("lookagent.loop", ["outcome verified", "lookagent demo complete"])
    expect("mediacost.cost", ["cost per resolved outcome: $0.0111", "mediacost demo complete"])
    expect("senseeval.harness", ["gate: FAIL", "vision-lowlight", "senseeval demo complete"])
    expect("sensesafe.filter", ["QUARANTINE", "sensesafe demo complete"])
    expect("parcelcapstone.capstone", ["verdict: SHIP", "parcelcapstone demo complete"])
    print()
    print("== direct assertions ==")
    from visiontriage.cascade import route
    check("cascade routes 0.90 to auto-decide", route(0.90) == "auto-decide")
    check("cascade routes 0.60 to vlm-review", route(0.60) == "vlm-review")
    check("cascade routes 0.30 to human-review", route(0.30) == "human-review")
    from crossmodal.search import rank
    check("crossmodal top hit is the red jacket", rank()[0][0] == "photo:red-jacket")
    from voiceloop.budget import total, STAGES
    check("voice loop fits its budget", total(STAGES) <= 1200)
    print()
    if FAILURES:
        print(f"OVERALL: FAIL ({len(FAILURES)} failures)"); return 1
    print(f"OVERALL: PASS ({COUNT[0]} checks)")
    return 0
if __name__ == "__main__": sys.exit(main())
