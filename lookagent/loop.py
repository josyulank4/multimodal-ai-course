"""Perceive-ground-act-verify agent loop with a step budget (Lesson 30)."""

SCREEN = {"refund_button": (0.72, 0.88), "approve_button": (0.25, 0.88)}
GOAL = "refund_button"
BUDGET = 5
TARGETS = {"refund_button": (0.72, 0.88), "approve_button": (0.25, 0.88)}


def perceive(screen):
    """The screen as it actually is: every visible control, by name."""
    return sorted(screen)


def ground(targets, goal):
    """Grounding is pointing: the goal's coordinates in the agent's
    map. The map is a belief — the screen is the fact."""
    return targets.get(goal)


def click(screen, point):
    """A click lands on the control actually at the point; if none
    is there, it lands on nothing — a misclick."""
    for name, coords in screen.items():
        if coords == point:
            return name
    return None


def verify(state, expected):
    """Verify in the record: the status the world holds now, checked
    against the status the act intended."""
    return state.get("status") == expected


def run(screen, targets=None, goal=GOAL, budget=BUDGET):
    """The loop as a loop: perceive, ground, act, verify — counted,
    and stopped by the budget, not by hope."""
    targets = SCREEN if targets is None else targets
    state = {"status": "open"}
    steps = []
    steps.append(f"perceive: claim screen captured ({len(screen)} controls)")
    steps.append(f"ground: {goal} at {ground(targets, goal)}")
    hit = click(screen, ground(targets, goal))
    steps.append(f"act: click {goal}")
    if hit == goal:
        state["status"] = "refund-issued"
    steps.append(f"verify: status changed to {state['status']}")
    hit_retry = None
    if not verify(state, "refund-issued"):
        steps.append("verify: NOT refund-issued - misclick caught by verification")
        steps.append(f"perceive again: controls are {perceive(screen)}")
        hit_retry = click(screen, ground(screen, goal))
        steps.append(f"act again: click {goal} at {ground(screen, goal)}")
        if hit_retry == goal:
            state["status"] = "refund-issued"
        steps.append(f"verify again: status is {state['status']}")
    for i, s in enumerate(steps, 1):
        print(f"step {i}: {s}")
    used = len(steps)
    if used > budget:
        print(f"agent stopped: {used} steps exceeds budget {budget} - no outcome claimed")
        return steps
    if verify(state, "refund-issued"):
        print(f"agent finished in {used} steps of {budget} budget \u2014 outcome verified")
    return steps


def drifted_run():
    """The long tail arrives: the vendor swapped the buttons, and the
    agent's map is now stale. The blind click hits approve; only
    verification stands between that and the customer."""
    moved = {"refund_button": (0.25, 0.88), "approve_button": (0.72, 0.88)}
    print("drift case: vendor swapped the buttons; the map is stale")
    run(moved, targets=TARGETS)


def main():
    run(SCREEN)
    drifted_run()
    print("lookagent demo complete")


if __name__ == "__main__":
    main()
