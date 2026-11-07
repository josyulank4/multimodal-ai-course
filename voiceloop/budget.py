"""Voice-loop latency budgeter: per-stage budgets vs turn limit (Lesson 14)."""
LIMIT_MS = 1200
STAGES = [("capture+vad", 120), ("streaming asr", 300), ("llm first token", 450), ("tts first audio", 250), ("network jitter", 60)]
def total(stages): return sum(ms for _, ms in stages)
def main():
    for name, ms in STAGES: print(f"{name}: {ms} ms")
    t = total(STAGES)
    print(f"voice loop total: {t} ms of {LIMIT_MS} ms budget")
    print("verdict: WITHIN BUDGET" if t <= LIMIT_MS else "verdict: OVER BUDGET")
    slow = STAGES + [("llm first token (cold)", 400)]
    t2 = total(STAGES) - 450 + 850
    print(f"cold-start variant: {t2} ms -> verdict: OVER BUDGET (fix: warm the model)")
    print("voiceloop demo complete")
if __name__ == "__main__": main()
