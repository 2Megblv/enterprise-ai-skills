# DEPRECATED

This folder is preserved for reference but is no longer the recommended path for generating decks from a storyline.

**Use instead:**
- [deck-pipeline](../deck-pipeline/SKILL.md) — the 4-agent strategist → builder → critic → fixer flow
- [mckinsey-charts](../mckinsey-charts/SKILL.md) — native python-pptx charts (editable inside PowerPoint, no third-party API)
- [storyline-builder](../storyline-builder/SKILL.md) — the storyline structure that feeds the pipeline

## Why this path was retired

The Gamma-based approach required an external account, an API key, per-deck credit cost, and produced decks where the audience could not easily edit the data inside individual charts. The native python-pptx path (via `mckinsey-charts`) gives:

- Editable PowerPoint chart objects (right-click → Edit Data works)
- No third-party dependency
- Consistent McKinsey-style defaults (single highlight color, no gridlines, claim-shaped titles)
- No per-deck cost

If you want to keep using Gamma for the AI-generated visuals (illustrations, photos), the code in this folder still works. For charts and structured slides, prefer the new path.
