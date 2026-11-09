# Initial collection validation

Date: 2026-11-10. Scope: the native ECL layers on `studio-ecl`.

## Commands and results

`python3 scripts/validate.py`

Result: 22 common maps and 44 name profiles pass native section separation,
matching key coverage, valid identifiers, unambiguous reverse names, global
type declarations, and basic native signature grammar.

Temporary damaged copies were rejected for missing opcode 23, duplicate
mnemonics, encoding sections inside a naming layer, and reserved identifiers.
The restored temporary copy passed. Separate temporary checks reject `Q`, `*`,
`S**f`, and `S*fS` as malformed signatures while accepting empty signatures,
`m*D`, `mS*D`, `SSS*H`, `fSf*H`, `nfffssS`, and `SSto`.

## Actual native map loading

A temporary C driver was compiled with GCC against unchanged files from the
pinned thtk checkout:

```sh
gcc -D_DEFAULT_SOURCE -ffunction-sections -fdata-sections \
  -I "$check_dir" -I "$thtk_dir/util" -I "$thtk_dir/thecl" \
  "$check_dir/native_check.c" "$thtk_dir/thecl/eclmap.c" \
  "$thtk_dir/util/seqmap.c" "$thtk_dir/util/util.c" \
  -Wl,--gc-sections -lm -o "$check_dir/native-check"
```

The driver uses the actual `eclmap_load`, `seqmap_get`, and mnemonic lookup. For
baseline comparisons, it compiles unchanged copies of the native C format tables
and their `find_format`, `th06_find_format`, `th06_find_timeline_format`, and
`th10_find_format` functions from that same checkout. Baseline lookup uses empty
map overrides, so this comparison does not merely read the just-loaded snapshot.

All 44 `(version, style)` combinations load. Their 35,284 emitted name/type/
signature entries match the ECLM contents, and all common encoding signatures
match the native compiler's lookup. The only emitted diagnostic is thtk's
existing warning that its signature validation is not implemented; the Python
validator checks the basic grammar independently. The temporary driver and
mutation fixtures are not project dependencies or a new permanent test harness.

The review confirmed the native fallback chains and identified the initial
validator's overly permissive signature expression. A temporary regression
check reproduced acceptance of `Q`; the validator was tightened, and invalid
examples now fail while all collection files pass.

Source inspection also found globals explicitly labelled ZECL in the upstream
maps. A temporary check reproduced leakage of TH20 ID `-9873` into the stock
layer. The import now excludes explicit ZECL blocks, including those globals;
TH18 ID `-9897` and TH20 ID `-9873` are absent, and all native loading checks
were rerun after that correction.

## Limits

- No ECL binary compile/decompile roundtrip or in-game behavior was tested.
- Compiler-known inherited entries are not proof of game-side implementation.
- Cross-version name correspondences and the source differences in
  `import-audit.json` have not all been independently reverse-engineered.
- No Studio product code, existing user configuration, or UI was changed.
- The collection is an initial reviewable baseline; unresolved names and
  third-party licensing clarification remain visible in the source records.
