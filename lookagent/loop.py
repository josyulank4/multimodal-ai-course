"""Perceive-ground-act-verify agent loop with a step budget (Lesson 30)."""

SCREEN = {"refund_button": (0.72, 0.88), "approve_button": (0.25, 0.88)}
GOAL = "refund_button"
BUDGET = 5
TARGETS = {"refund_button": (0.72, 0.88), "approve_button": (0.25, 0.88)}

# START SCAFFOLD — Lesson 30 builds the loop as functions:
#   perceive(screen)  -> the visible control names
#   ground(targets, goal) -> the goal's coordinates in the map
#   click(screen, point)  -> the control actually at the point
#   verify(state, expected) -> the status check, in the record
#   run(screen, ...)  -> perceive, ground, act, verify, counted,
#                        and stopped by the budget
#   drifted_run()     -> the vendor swapped the buttons; the map
#                        is stale; verification must catch it
# TODO: implement the five functions; keep main() printing the
# shipped step lines and "lookagent demo complete".
