# Prompts: replicate this end-to-end

Copy these into Claude (or any LLM with these skills loaded) to reproduce the workflow. The skills referenced are in this repo — clone first so they auto-load in Claude Code, or paste the relevant `SKILL.md` contents as context for other LLMs.

---

## Step 1 — Issue tree

```
Use the issue-tree-builder skill.

Governing question: Which sport should I pick up as a 30+ adult who'll
actually stick with it for 5+ years?

Decompose into 3 MECE branches and 2-3 sub-branches each. Each terminal
branch should be a testable hypothesis, not a question. Prioritize which
branch to test first and why.
```

**Output:** see [01-issue-tree.md](01-issue-tree.md)

---

## Step 2 — Storyline

```
Use the storyline-builder skill.

Take the issue tree from step 1 and produce an 8-slide storyline. Every
slide title must be a claim with a specific number, not a topic. Group
into Situation / Complication / Resolution. The final slide must be
the recommendation in one sentence.

Compare: pickleball, tennis, running.
```

**Output:** see [02-storyline.md](02-storyline.md)

---

## Step 3 — Charts

```
Use the mckinsey-charts skill.

Generate three charts for the slides that need them:

1. Bar+callout: "Hours to feel competent" — pickleball 6, running 10,
   tennis 40. Highlight pickleball. Title is the claim, not the topic.

2. Waterfall: Annual cost bridge for pickleball — starter gear $60,
   lessons $120, league fees $150, court time $120, total $450.

3. Stacked column over time: weekly time mix (lessons / play / travel)
   for pickleball, by quarter, across Year 1.

Output: native python-pptx chart objects (editable inside PowerPoint).
```

**Code:** see [build.py](build.py) — the generator script.
**Output:** see [03-final-deck.pptx](03-final-deck.pptx).

---

## Step 4 — Deck pipeline

```
Use the deck-pipeline skill.

Take the storyline from step 2 and the charts from step 3. Run the
four-agent pipeline:

- Strategist: confirm audience (myself, deciding for a 5-year hobby
  commitment) and the governing thought
- Builder: produce the 8-slide .pptx using python-pptx + the charts
  from mckinsey-charts
- Critic: review the deck like a McKinsey EM — grade and identify top 3 fixes
- Fixer: apply the top 3 fixes and produce the final deck

Final output: a polished 8-slide .pptx with native editable charts.
```

**Output:** [03-final-deck.pptx](03-final-deck.pptx) — the final deck after critique.

---

## Reusing this workflow on your own decision

The structure is decision-agnostic. Swap the governing question and rerun:

- "Should I learn pickleball or padel?"
- "Which side project should I commit to this year?"
- "Should I take the new job or stay?"
- "Which neighborhood should I move to?"

Same 4 skills, same 8-slide arc, same chart slots. The deck takes ~30 seconds of prompting and produces a `.pptx` you can hand to anyone.
