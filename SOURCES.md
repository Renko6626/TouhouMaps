# Sources and import decisions

This document records the initial stock ECL snapshot. The maintained sources
of truth are the native `.eclm` files; the audit JSON files describe this import,
not a second editable encoding schema or a runtime generation input.

| Source | Fixed revision | Used for |
| --- | --- | --- |
| [zero318/TouhouMaps](https://github.com/zero318/TouhouMaps/tree/0673f4221f5e975842162e07cd7b765fc7570ebd) | `0673f4221f5e975842162e07cd7b765fc7570ebd` | Names and global types; prefer `_thtk.eclm` where present |
| [Priw8/eclmap](https://github.com/Priw8/eclmap/tree/f146162e330c27d1b0a8880c3a41884615147a11) | `f146162e330c27d1b0a8880c3a41884615147a11` | Names and additional global declarations from `eclmap/` |
| [thpatch/thtk](https://github.com/thpatch/thtk/tree/892114a0fcaa0bbdaaecf3cb4ad56f758683fb40) | `892114a0fcaa0bbdaaecf3cb4ad56f758683fb40` | Native regular/timeline instruction signatures and version lookup rules |

## Encoding definitions

`common/` snapshots the actual native tables and fallback logic in
`thecl/thecl06.c` and `thecl/thecl10.c`. Within one C table, the first matching
row wins (`util/value.c::find_format`); across version fallback tables, the
newer matching table wins. TH095 regular instructions fall back to TH08;
TH095 timeline instructions follow the separate TH09/TH08 timeline chain.
TH103 uses the `alcostg_fmts` table and TH10 fallback.

No truth signature attributes were stripped or mechanically translated. Native
thecl signatures were selected as the initial encoding baseline even when a
zero318 `_thtk` file differed. The audit records 228 such differences. Some are
representation choices, while others could reflect upstream fixes or custom
extensions. They have not been independently resolved by game disassembly.
This choice reproduces the pinned compiler's default lookup; it is not a claim
that all map overrides are wrong or that native thtk is correct for every game
instruction.

The fallback tables include inherited opcodes that a particular game may no
longer implement. Their neutral names mean "known by the pinned compiler's
lookup", not "tested executable instruction in this game". Out-of-table
upstream names/custom extensions are excluded and listed in the audit.
Explicit `# ZECL` blocks are also excluded, including their global declarations;
the block ends at the next map section or named instruction section. These
exclusions are recorded under `zecl_exclusions` in the import audit.

Global types prefer zero318's declarations, then add Priw8 declarations for
otherwise missing IDs; missing types are `?`. Both upstreams disagree about
ID `-9961` in TH10, 11, 12, 15, 18, and 185 (`$` versus `%`). The common layer
currently preserves zero318's `$` under that source-priority rule. These six
disagreements are listed in the audit and are not presented as newly verified
reverse-engineering results.

## Naming profiles

zero318 supplies source profiles for 15 target versions. Priw8 supplies profiles
for TH08, 11, 12, 13, 14, 15, 16, 165, 17, 18, and 185. Priw8's README declares
TH10 uses TH11's map, TH128 uses TH12's map, and TH143 uses TH14's map; this reuse
is explicit in the profile audit. The dedicated TH165 file takes precedence
over the README's older suggestion to reuse TH16.

Missing names may be filled from an unambiguous correspondence observed in
overlapping sources, restricted to the same generation (TH06–095, TH10–128,
TH13 onward) and the same native parameter signature or global type. Unknown,
internal `__...`, and numbered special/debug names are not correspondence
evidence. Each synthesized name records its other-style source name and donor
version/ID in `docs/import-audit.json`; this is evidence for a naming extension,
not an independent proof of equivalent game behavior.

Where no unique correspondence exists, the fork uses neutral names. Inferred
names that collide with an existing name also fall back to neutral names.
Native thecl keywords must be escaped by a descriptive prefix (`loop` becomes
`ecl_loop`); such spelling adjustments are recorded rather than silently
claiming byte-identical upstream naming.

The import was a one-time source inspection and snapshot. There is no supported
regeneration command, automatic upstream merge, or live dependency download.
Maintain the ECLM files directly and document subsequent source-backed changes.

## Licensing provenance

- zero318/TouhouMaps supplies its original files under the root `LICENSE`
  (Unlicense). Its root map files are preserved byte-for-byte.
- thtk's native signature-table snapshot retains the upstream notice in
  `licenses/thtk.COPYING`.
- The pinned Priw8/eclmap repository has no explicit license file or license
  statement. Its names remain attributed to that source. This fork does not
  represent those third-party contributions as having been relicensed under
  zero318's Unlicense; permission for downstream redistribution remains to be
  clarified before Studio bundles this baseline.

No private game binaries, original game scripts, or extracted game assets are
included in this collection.
