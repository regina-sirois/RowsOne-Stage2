---
name: update-docs
description: >-
  Sync README.md with the project’s actual behavior (CLI flags, setup, tests,
  hooks, skills). Use when main.py, pyproject.toml, tests, githooks, or project
  skills change, when documentation may be stale, or when the user asks to
  update docs/README.
disable-model-invocation: false
---

# Update Docs

Keep `README.md` accurate against the codebase. Prefer small, targeted edits over rewrites.

## When to run

Apply whenever project behavior or developer workflow changed in a way readers would notice—especially after edits to `main.py` argparse/behavior, dependencies, tests, `.githooks/`, or `.cursor/skills/`.

## Instructions

1. **Read sources of truth** (as needed):
   - `main.py` — CLI flags, defaults, print/filter behavior
   - `pyproject.toml` / `uv.lock` — runtime deps and Python version
   - `tests.py`, `.githooks/pre-commit` — how to run/verify tests
   - `.cursor/skills/*/SKILL.md` — skills called out in the README
2. **Diff against `README.md`**. Check at least:
   - [ ] Setup / install (`uv sync`, Python version) still correct
   - [ ] Pipeline summary matches `main.py` (grouping, lists, classification, STOP skipping, summary block rules)
   - [ ] Every CLI flag is documented (examples + flags table); remove or mark flags that no longer exist
   - [ ] Flag interactions that matter are noted
   - [ ] Example output still reflects current formatting (or is clearly marked as illustrative)
   - [ ] Skills, tests, and pre-commit hook sections match the repo
3. **Edit `README.md` only** unless the user asks to touch other docs.
4. **Guardrails**:
   - Do not document unimplemented features
   - Do not invent flags, deps, or workflows
   - Preserve existing voice/structure; fix discrepancies rather than restyle
   - Keep Markdown valid (links, tables, fenced code)
   - Do not commit unless asked
   - Do not update the output section to include any real phone numbers or names
5. **Briefly report** what was outdated and what you changed (or that docs were already current).

## Example

`main.py` adds `--report` and skips the summary when set → README invocation examples and flags table gain that flag; note where the report is generated

## Done when

`README.md` matches current project behavior for the areas above, or you confirmed no doc updates were needed.
