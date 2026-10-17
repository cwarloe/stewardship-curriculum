# Agent / LLM handoff — Stewardship Curriculum

Read this before working in the repo. [`DECISIONS.md`](DECISIONS.md) wins if anything here conflicts.

## What this is

A seminar for 5–10 adults: an online kickoff, work at home, an in-person weekend, and follow-up. The goal is **changed practice** in how people steward time, treasure, and talents, not just knowledge about stewardship. The research is clear that knowledge alone rarely changes behavior ([R001](research/R001-what-research-applies.md)).

## The three things that get violated most

1. **Theology is author canon.** Doctrine, how a passage is applied, positions on tithing, giving, work, and rest: the author states these, and nobody else fills them in. If a session needs a theological claim the author hasn't made, write `[UNKNOWN — author]` and ask. A plausible-sounding answer is worse than a gap here.
2. **Every design claim cites its evidence and confidence.** "Groups work better at 6" needs a research record behind it, or it gets labeled as a judgment call. Use the confidence scale in [`research/PROTOCOL.md`](research/PROTOCOL.md). "No evidence exists" is a finding; write it down.
3. **Source material is verbatim.** Nothing in [`source-material/`](source-material/) gets edited, not even typos. Quote it, excerpt it, or build from it somewhere else.

Tag assertions in design docs: `[AUTHOR]` (the author stated it) / `[DERIVED]` (give the derivation) / `[OPTION]` (not decided) / `[UNKNOWN]` (ask, don't fill).

## Design rules carried over from sibling projects

- **Practice before teaching.** The home work produces the person's own evidence (their week, their spending, their gifts) before the weekend interprets it.
- **Predict, then check.** Before any log, the person writes down what they expect to find. (From NADF R006: retrieval with feedback built in.)
- **Every story or illustration carries a point, or it comes out.** Seductive details reduce learning while making material feel better. (From NADF's training-design skill.)
- **Worked example, guided practice, the person's own work.** A case study shows the move, discussion practices it, and the person's own plan is the evidence.
- **Don't add process.** No review gates or registers nobody will run. Put a lesson where the next person will trip over it.

## Research workflow

[`research/PROTOCOL.md`](research/PROTOCOL.md). Short version: frame the question, search reproducibly, record whether a source was actually *read* or only found, paraphrase, and give a confidence rating. If an external model is asked a research question, keep the prompt verbatim in `research/prompts/`.

## Done definition

A session design is done when:
- every timing and format choice traces to a research record or is labeled a judgment call
- every theological claim is `[AUTHOR]`
- it names what would show that it isn't working
- the author has approved it
