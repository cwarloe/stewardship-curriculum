# Decisions

Short records. What was decided, why, and what would reopen it.

**These are defaults, not laws.** Each decision describes the default behavior. Overriding one is fine when there's a compelling practical, operational, or ministry reason. Write the reason down where the override happens, so the next person can see why the default didn't apply.

## ADR-001 — Format: kickoff → between-work → weekend → follow-up

**Decided 2026-09-29 by the author.** An initial meeting (possibly live online), work done at home between sessions, an in-person weekend seminar (Friday night and Saturday) with extended conversation, then some form of follow-up.

**Why:** The author's design. It also matches the evidence: spaced exposure beats one massed session, and single-sitting effects fade within weeks without reinforcement ([R001](research/R001-what-research-applies.md) §1, §2).

**Reopen if:** follow-up proves impossible to sustain. Without it, the evidence says the weekend's effects largely fade.

**Partly superseded by ADR-008 (2026-10-18):** the kickoff is an in-person lunch after church, not an online meeting. The rest of the format stands.

## ADR-002 — Group size 5–10

**Decided 2026-09-29 by the author.** Minimum about 5, typical maximum 8–9, and up to 10 only when couples are included. Larger is outside the default and needs a compelling reason.

**Revised 2026-10-21 by the author:** the pilot runs with **4–8 participants**, and **up to 10** if that many complete the qualifying task (ADR-008). At 9–10, split the discussion segments as below.

**Implication [DERIVED]:** at 9–10, discussion segments should split into two sub-groups. At 5, group discussion behaves like dialogue; at 10, like serial monologue dominated by the loudest voice ([R001](research/R001-what-research-applies.md) §4).

## ADR-003 — Research sets the timelines

**Decided 2026-09-29 by the author.** Gap lengths, follow-up cadence, and session structure come from research, not intuition. Where research is silent, say so and label the choice a judgment call.

## ADR-004 — Theology is author canon

**Decided 2026-09-29; softened 2026-10-21 by the author.**

**Default:** doctrine, Scripture choices and applications, and positions on giving, work, and rest come from the author.

**Override:** when the author asks for a draft, an LLM may write theological content. It's marked `[DRAFT]` and isn't final until the author approves it. Example: the expanded reset statement in [`curriculum/02-friday-night-reset.md`](curriculum/02-friday-night-reset.md) §3C was drafted on request.

See [AGENTS.md](AGENTS.md).

## ADR-005 — Pilot audience: single adults

**Decided 2026-09-29 by the author; revised 2026-10-21.** The pilot is open to **single adults, men and women**. (Originally men only. The author: some women may join the pilot, "and that's a good thing.") All materials use "participants," not "men." Couples are expected in later runs.

`[DERIVED — confirm]` "Single" is kept from the original decision, because the reason below still applies. The author hasn't restated it.

**Why:** It's simpler for the pilot. One person's budget, one person's calendar, one person's gifts, with no household negotiation inside each of the three areas. It also matches the voice of the essay in `source-material/`.

**Implications [DERIVED]:**
- There's no spouse at home to support follow-up, so that support has to come from the group. Pair participants with each other for the check-ins ([R001](research/R001-what-research-applies.md) §3).
- Pilot results say little about couples. Budgets and calendars that two people share are a different problem, so treat couples as a new design question when they come, not as a reuse of the pilot.

**Reopen when:** the pilot has run and there is something to learn from it.

## ADR-006 — Timeline adopted

**Decided 2026-09-29 by the author**, adopting the timeline derived in [R001](research/R001-what-research-applies.md):
- online kickoff
- **4–5 weeks** of pre-work
- the weekend
- **12 weeks** of follow-up

**Follow-up load:** five contacts, not twelve weekly meetings.
- Short pair check-ins at weeks 1, 2 and 3
- Group touchpoints at weeks 6 and 12
- A shortened re-log at week 12

The weekly habit is each participant's own chosen behavior, not a program meeting.

**The author's concern, recorded:** 12 weeks is a big ask. He accepted it because the habit research (R001 §2) puts the average at about 66 days. **Reopen if** pilot participants drop out of the follow-up. Cut contacts before cutting length: the early check-ins carry the most weight.

**Partly superseded by ADR-008 (2026-10-18):** the pre-work is now the lunch, then three short weekly tasks, with the weekend in week 4. That replaces the 4–5 weeks of logging. The kickoff-to-weekend gap is about 4 weeks, still in R001's acceptable range. The month of spending data that pushed the gap longer now comes from the bank's 30-day history instead of live logging. **The 12-week follow-up stands.**

## ADR-007 — Sequence: reset, then plan, then behavior

**Decided 2026-09-29 by the author.** The seminar produces a change in perspective first, which makes participants motivated learners and actors. That change then leads to an action plan and changed behavior. The focus is stewardship of **time, treasure, and talents** together, **not money first**.

**How the research shapes it [DERIVED], from [R002](research/R002-mindset-before-behavior.md):**
- **A reset alone moves behavior only modestly** (the intention–behavior gap). Saturday must end in if-then plans the same weekend.
- **The pre-work's predict-then-check steps are the trigger for the reset,** not just preparation. Every door and every weekly task in ADR-008 has one. The gap between what someone predicts and what they find is their own disorienting dilemma, the experience that doesn't fit how they've been seeing things.
- **Invite; don't shame.** Motivation from guilt doesn't last. Each participant chooses their own commitments.
- **The reset is an identity shift** (steward, not owner). That makes hard weeks read as meaningful rather than as failure.

**Author's refinement (2026-10-18): "Light a candle" (embodied action before heart understanding)**
- Like lighting a candle to enter an ancient practice, taking concrete, physical action creates movement before full intellectual or spiritual comprehension arrives.
- The 3-week pre-retreat sprints are small behavioral acts ("lighting the candle"). The retreat weekend is where participants sit down to ask: *What did that mean? Who am I? Who owns this?*
- Action precedes reflection; reflection transforms the heart and anchors identity.

## ADR-008 — Onboarding: Post-service lunch, "Light a Candle" sprints, and earned self-selection

**Decided 2026-10-18 by the author.** 

1. **The Kickoff is a Post-Service Lunch:** Rather than a cold online call, the kickoff is an informal 35-minute post-service lunch at church (pizza/tacos). People are already present, hungry, and in a shared space.
2. **The "No Hostages" Doctrine (Autonomous Motivation):** We do not take sign-ups at lunch. People can't be coerced by parents, pastors, or guilt (controlled motivation). "Hostages don't form habits." We seek honest, hungry drifters who want order and purpose.
3. **The 45-Minute Quick-Win Gate (Earned Self-Selection, per `mr-life-manager` ADR-015):** The lunch hands each person a 3-Door Menu (Time, Treasure, Talent). Each person chooses **one** acute pain point to tackle in 45 minutes or less before Tuesday night. Completing this single action is their ticket to a seat in the weekend cohort: 4–8 seats, up to 10 if that many finish (revised 2026-10-21; originally 6–8).
4. **The 3-Week Progressive Runway ("Light a Candle" Sprints):**
   - **Week 1:** Choose Door 1 (Primary Pain) → 45-min win → Qualifies for Cohort.
   - **Week 2:** Breadth Sprint in Domain B (20–30 min win) → Reclaim margin / eliminate leaks.
   - **Week 3:** Breadth Sprint in Domain C (20–30 min win) → Assemble personal 3-T baseline dossier.
   - **Week 4:** The In-Person Weekend Retreat (Heart, theology, identity reset, strategic 90-day plan).
   - This replaces 4–5 weeks of grueling prospective daily logging with three satisfying, bite-sized wins while preserving the required spacing.

## ADR-009 — Principles and practices, not requirements

**Decided 2026-10-21 by the author.** The ethos across the whole seminar is **principles and practices, not rigid, inflexible requirements.** No legalistic quotas, such as "you must have X hours" or a fixed percentage. The work is to get participants to dig into how they actually spend their time, treasure, and talents, and then to **think, read, and pray** their way to their own practices.

**Fits the research:** chosen commitments outlast pressured ones (R002 §2), and the predict-then-check tasks already put participants' own evidence in front of them (R002 §4).

**Applies to:** every session, worksheet, and the follow-up. When a draft prescribes a number, ask whether it's an example or a requirement. Examples are fine; requirements need a compelling reason (see the note at the top of this file).

## ADR-010 — Sabbath and rest: a principle, with each participant choosing the practice

**Decided 2026-10-21 by the author** (option A of the three proposed). Rest is part of stewarding **time**, and follows ADR-009:
- **Present rest as received, not as a test.** It's a principle, not a quota. No prescribed hours or day.
- **Participants examine their own rhythm first,** with a predict-then-check question: "When did I last fully stop?"
- **Read, discuss, pray.** Participants read a small set of passages on rest, discuss what they notice, and pray. The passages are the author's to choose (open below).
- **Each participant chooses one practice of their own,** such as a weekly stretch of rest, an evening without screens, worship, or unhurried time with people.
- **The facilitator can say honestly that Christians hold different views on Sabbath,** without settling that debate in the room.

**Rejected:** B, a weekly Sabbath day offered as an invitation (leans prescriptive), and C, no rest content before Saturday (loses the predict-then-check).

**Already reflected in:** the Week 2 Time task and the baseline summary sheet in [`curriculum/01-light-a-candle-sprints.md`](curriculum/01-light-a-candle-sprints.md).

---

## Open decisions

Things the author needs to decide. Nothing downstream should assume an answer.

- **Position on giving.** Tithe as a standard, a starting point, or not prescribed? This shapes the treasure session. `[UNKNOWN — author]`
- **Does the mind map survive?** [`outline/curriculum-mindmap.md`](outline/curriculum-mindmap.md) predates the seminar format and has seven Act II branches for roughly four weekend sessions.
- **Follow-up owner.** Who runs the check-ins: the facilitator or pairs of participants? This decides whether the boosters in R001 actually happen.
- **The core of the reset.** What should a participant believe differently by the end of Friday night? This is the theological center of the seminar, and everything on Saturday hangs from it.

  **Author's brainstorm draft (2026-09-29), verbatim, not yet locked:**
  > "everything I have belongs to God. He is loaned it to me and asked me to be a good steward of it. That includes my time my treasure and my talents. None of it is mine. Because this is who I am I'm seeking to figure out what does it mean for me to steward these resources? How shall I invest them? How do I spend my money how do I spend my time how do I use my gifts?"

  Structure as drafted: **belief** (God owns everything; it is on loan) → **identity** ("this is who I am") → **three open questions** (money, time, gifts). The questions line up with Saturday's three sessions. `[AUTHOR — draft]`

  An expanded version, drafted at the author's request, is in [`curriculum/02-friday-night-reset.md`](curriculum/02-friday-night-reset.md) §3C. `[DRAFT]`
- **Fewer than 4 qualify.** Run the weekend anyway, postpone it, or reopen the lunch invitation? (The seat range itself is settled: ADR-002 and ADR-008.)
- **Passages on rest.** Which Scripture participants read on rest (ADR-010). `[UNKNOWN — author]`
- **Weekend date.** `[OPTION]` Just before a natural fresh start (the start of a month, a new year, or a season), so the plans begin on a landmark ([R002](research/R002-mindset-before-behavior.md) §5).
