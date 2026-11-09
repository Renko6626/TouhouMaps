# ECL collection implementation plan

> **For agentic workers:** Use superpowers:executing-plans inline. Steps use checkbox syntax for tracking. User instructions on scope and verification override skill defaults.

**Goal:** Deliver a reviewable native ECL map collection covering Studio's 22 versions with shared signatures and two name profiles.

**Architecture:** Keep upstream root files; add `common/` and `names/{zero318,priw8}/`. Native thecl loads the common layer then one name layer. No runtime generator or intermediate authoring format.

**Tech Stack:** Native ECLM data, Python 3 standard library for validation, existing thtk C map loader for compatibility verification.

**Spec:** `docs/superpowers/specs/2026-11-10-ecl-collection-design.md`

## Global constraints

- Target versions: 6, 7, 8, 9, 95, 10, 103, 11, 12, 125, 128, 13, 14, 143, 15, 16, 165, 17, 18, 185, 19, 20.
- Original root maps stay intact; no compiler patch, binary reverse engineering, dependency install, app UI changes, or CI.
- Native data is authoritative after import; source audit output is provenance, not a second authoring format.
- No inferred binary signature or invented behavior. Unresolved names are neutral and traceable.

## Review focus

- Early-game timeline signatures differ from regular ECL and must retain their namespace.
- thtk fallback tables contain inherited entries; compiler-known coverage does not prove a game implements every opcode.
- Shared Priw8 maps for 12.8 and 14.3 must be labelled as upstream-declared reuse.
- Mnemonic or register collisions must not silently change a reverse mapping.
- Missing upstream style profiles must be labelled as fork-owned naming extensions.

### Task 1: Shared stock signatures and source baseline

**Files:** `common/thXX.eclm`, `SOURCES.md`, `licenses/thtk.COPYING`.

**Interfaces:** Produce one native map per target version, containing only `ins_signatures`, `timeline_ins_signatures`, and `gvar_types`. Source keys are version and opcode/register, never translated names.

- [x] Pin zero318, Priw8, and thtk source commits and record source selection.
- [x] Snapshot native thtk signatures using the fallback rules in `th06_find_format`, `th06_find_timeline_format`, and `th10_find_format`; preserve empty signatures.
- [x] Merge global type declarations from available upstream maps; record disagreements and chosen source explicitly.
- [x] Inspect signatures for TH06/08/12/13/18/19/20 against upstream definitions.

### Task 2: Both native name profiles

**Files:** `names/zero318/thXX.eclm`, `names/priw8/thXX.eclm`, `docs/coverage.md`, `docs/import-audit.json`, `README.md`.

**Interfaces:** Exactly two name maps per version, with `ins_names`, `timeline_ins_names`, and `gvar_names` only; every declared name points to a key in that version's common layer.

- [x] Preserve available upstream names and collect unambiguous name correspondences from overlapping profiles.
- [x] Fill missing style profiles using only those correspondences; label unmatched keys with neutral names and record the outcome per entry.
- [x] Exclude custom/out-of-table instructions; resolve identifier collisions visibly in the audit.
- [x] Document loading order, coverage, synthesized-name counts, source/licensing limits, and the Studio follow-up boundary.

### Task 3: Validate and publish a review branch

**Files:** `scripts/validate.py`, `docs/validation.md`.

**Interfaces:** `python3 scripts/validate.py` returns nonzero for invalid native sections, missing profiles/coverage, ambiguous identifiers, or invalid types. No third-party Python packages.

- [x] Add the small validator against the actual `.eclm` files, with specific TH18 style examples and early timeline checks.
- [x] Run it against valid files and temporary broken copies to prove meaningful failures without keeping duplicate tests.
- [x] Compile the pinned upstream map loader with a temporary driver and load all 44 common/name combinations; inspect diagnostics and selected loaded values.
- [x] Review data/provenance and the complete diff; record actual checks and limitations.
- [x] Commit and push `studio-ecl` to the user's new fork without changing upstream root maps or the default branch.
