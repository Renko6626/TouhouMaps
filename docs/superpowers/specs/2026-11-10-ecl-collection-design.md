# ECL collection design

Status: repository layering approved in the Studio conversation on 2026-11-10.
Semantic research and product integration are deferred by the user's later
decision. The initial import at `39a2956` remains a provisional snapshot; its
native thtk signature priority, generated names, and inferred correspondences
are not individually approved or behaviorally validated. See the
[research handoff](../../research-handoff-2026-11-10.md) before resuming.

## Purpose and scope

Maintain a Studio-owned fork of zero318/TouhouMaps with native thecl ECLM
profiles for the 22 ECL game versions already supported by Studio:
6, 7, 8, 9, 95, 10, 103, 11, 12, 125, 128, 13, 14, 143, 15, 16, 165,
17, 18, 185, 19, 20. Trial releases, TH06NC, ZECL extensions, and new binary
reverse engineering are outside this initial collection.

The upstream root files stay intact. Work lives on `studio-ecl`; Studio can
pin a reviewed commit independently of upstream updates.

## Approaches and decision

Maintaining two complete map sets makes each file standalone, but duplicates
signatures and variable types. A new intermediate schema plus a generator
would deduplicate them at the cost of a new authoring format and toolchain.
The accepted approach uses native ECLM layers: `common/thXX.eclm` owns
signatures and global types, and `names/{zero318,priw8}/thXX.eclm` owns names.
Load the common map first and exactly one name profile second with `-m`.

## Data rules

- Treat `(game version, instruction namespace, opcode)` as identity; global
  variables use `(game version, register ID)`. Names do not identify an opcode
  across game versions.
- Snapshot native encoding signatures from pinned thtk tables and their actual
  version fallback rules. Do not translate truth signature attributes by
  stripping text or guess a binary encoding from a mnemonic.
- Keep upstream names when available for that style/version. A counterpart
  name may be reused only when the same source name has an unambiguous
  correspondence in overlapping upstream profiles. Record synthesized names
  as fork-owned style extensions, not as upstream definitions.
- Unresolved names remain neutral (`unknown_<opcode>` / `unknown<opcode>`;
  corresponding neutral global names). Do not invent instruction behavior.
- Do not copy out-of-table custom instruction extensions into the stock
  profiles. Record exclusions and signature disagreements for review.
- Preserve source revisions, licensing information, and per-profile provenance.
  Priw8's upstream has no explicit license file; do not apply zero318's
  Unlicense to third-party material by implication.

## Responsibility boundaries

This phase ships the independent data repository, usage documentation, and a
small validator. It does not change the compiler, create a runtime service,
introduce a metadata authoring schema, or add CI. Studio's UI/configuration
integration follows after the data baseline is reviewable; that integration
must make compilation, decompilation, editor vocabulary, and MCP use the same
version and style and must preserve explicit custom-map choices.

## Verification

Check all 22 versions in both styles for valid native sections, matching opcode
coverage, valid and unambiguous identifiers, known variable types, and the
separation of names from encoding definitions. Verify the layers with the real
thtk map loader. Inspect representative TH06/08/12/13/18/19/20 source entries.
Loading maps is not a binary roundtrip or an in-game behavior acceptance test.
