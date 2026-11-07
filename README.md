# Multimodal AI in Production — Companion Code (Udemy Course 7)

Working, stdlib-only Python demos for every hands-on lesson of the course.
No API keys, no third-party packages: every mechanic runs offline so students
see what the production tools actually compute.

## Run the full validation
```
python validate.py
```
Expected final line: `OVERALL: PASS`.

## Packages (one per DEMO lesson)
| Package | Lesson | What it shows |
|---|---|---|
| visiontriage | 10 | Damage-triage cascade: cheap first, VLM on doubt |
| voiceloop | 14 | Voice-loop latency budget vs the turn-taking limit |
| docintel | 18 | Invoice extraction with schema + field confidence |
| crossmodal | 22 | Cross-modal retrieval in one shared space |
| fusiongate | 26 | Weighted fusion with a disagreement gate |
| lookagent | 30 | Perceive-ground-act-verify agent loop |
| mediacost | 34 | Cost per resolved outcome for a media queue |
| senseeval | 38 | Per-slice evaluation harness + release gate |
| sensesafe | 42 | Media-is-data safety filter for hostile uploads |
| parcelcapstone | 46/51 | The parcel system, end to end + storm sizing |

## Lesson tags
Each DEMO lesson is tagged in this repo: `lXX-start` (code before the lesson's
build) and `lXX-finish` (the exact code the lesson ships). Tags are added as
each DEMO lesson is produced; the pilot (Lesson 1) is a theory lesson and
carries no tag.
