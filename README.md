# Stewardship: Living as God's Stewards

A small-group seminar on stewarding time, treasure, and talents under God's ownership.

**Format** ([ADR-001](DECISIONS.md#adr-001--format-kickoff--between-work--weekend--follow-up)): an online kickoff, work done at home between sessions, an in-person weekend (Friday evening and Saturday), then structured follow-up. **Group size:** 5–10 people ([ADR-002](DECISIONS.md#adr-002--group-size-510)). **Pilot:** single men only; mixed groups and couples come in later runs ([ADR-005](DECISIONS.md#adr-005--pilot-audience-single-men)).

**Research-driven** ([ADR-003](DECISIONS.md#adr-003--research-sets-the-timelines)): timelines and session design come from the evidence in [`research/`](research/), with its confidence stated. Theology is the author's, never the machine's ([ADR-004](DECISIONS.md#adr-004--theology-is-author-canon)).

## Layout

```
AGENTS.md          # playbook for anyone (human or LLM) working in this repo
DECISIONS.md       # what's been decided, and what's still open
curriculum/        # session guides, participant worksheets, and onboarding tools
outline/           # the original Act I–III mind map (draft, predates the seminar format)
research/          # protocol, evidence index, research records
source-material/   # the author's original writing, kept verbatim
scripts/           # repo checks CI runs (links, evidence index)
.github/ISSUE_TEMPLATE/  # issue templates: lesson requests and bug/typo reports
```

## Status

Active curriculum drafting. Onboarding, qualification model, and pre-retreat runway adopted ([ADR-008](DECISIONS.md#adr-008--onboarding-post-service-lunch-light-a-candle-sprints-and-earned-self-selection)). The post-service lunch guide, 3-door menu, pre-retreat sprints, and Friday night reset session are drafted in [`curriculum/`](curriculum/). The next step is drafting the Saturday deep-dive sessions (Time, Treasure, Talent) and the 12-week pair booster guides.

## Notes

- File a lesson idea or a typo through the issue templates in `.github/ISSUE_TEMPLATE/`.
- CI checks that local Markdown links and `#anchors` resolve, and that `research/EVIDENCE_INDEX.md` has one row per research record with a matching link and status. Run `python3 scripts/check_links.py` and `python3 scripts/check_evidence_index.py` locally before pushing.
