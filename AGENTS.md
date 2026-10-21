# Agent / LLM handoff — Stewardship Curriculum

Read this before working in the repo. [`DECISIONS.md`](DECISIONS.md) wins if anything here conflicts.

**Everything here is a default, not a law.** Follow the default unless there's a compelling practical, operational, or ministry reason not to. When you override one, write the reason down where the override happens.

## What this is

A small-group seminar (5–10; the pilot is up to 8 single men): a lunch after church as the kickoff, three weeks of short tasks, an in-person weekend, and 12 weeks of follow-up ([ADR-008](DECISIONS.md#adr-008--onboarding-post-service-lunch-light-a-candle-sprints-and-earned-self-selection)). The goal is **changed practice** in how people steward time, treasure, and talents, not just knowledge about stewardship. The research is clear that knowledge alone rarely changes behavior ([R001](research/R001-what-research-applies.md)).

## The three defaults that matter most

1. **Theology comes from the author.** Doctrine, how a passage is applied, positions on tithing, giving, work, and rest. If a session needs a theological claim the author hasn't made, write `[UNKNOWN — author]` and ask. **Override:** when the author asks for a draft, write it and mark it `[DRAFT]` until he approves it.
2. **Every design claim cites its evidence and confidence.** "Groups work better at 6" needs a research record behind it, or it gets labeled as a judgment call. Use the confidence scale in [`research/PROTOCOL.md`](research/PROTOCOL.md). "No evidence exists" is a finding; write it down.
3. **Source material stays verbatim.** Quote it, excerpt it, or build from it somewhere else. **Override:** a clear conversion error, such as RTF debris, can be fixed if the change is noted in [`source-material/README.md`](source-material/README.md).

Tag assertions in design docs: `[AUTHOR]` (the author stated it) / `[DRAFT]` (written on request, awaiting the author's approval) / `[DERIVED]` (give the derivation) / `[OPTION]` (not decided) / `[UNKNOWN]` (ask, don't fill).

## Design rules carried over from sibling projects

- **Practice before teaching.** The home work produces the person's own evidence (their week, their spending, their gifts) before the weekend interprets it.
- **Predict, then check.** Before any task, the person writes down what he expects to find. (From NADF R006: retrieval with feedback built in.)
- **Every story or illustration carries a point, or it comes out.** Seductive details reduce learning while making material feel better. (From NADF's training-design skill.)
- **Worked example, guided practice, the person's own work.** A case study shows the move, discussion practices it, and the person's own plan is the evidence.
- **Don't add process.** No review gates or registers nobody will run. Put a lesson where the next person will trip over it.

## Research workflow

[`research/PROTOCOL.md`](research/PROTOCOL.md). Short version: frame the question, search reproducibly, record whether a source was actually *read* or only found, paraphrase, and give a confidence rating. If an external model is asked a research question, keep the prompt verbatim in `research/prompts/`.

## Done definition

A session design is done when:
- every timing and format choice traces to a research record or is labeled a judgment call
- every theological claim is `[AUTHOR]`, or `[DRAFT]` with the author's sign-off
- it names what would show that it isn't working
- the author has approved it
