# Initial ECL coverage

All 22 versions have a native common layer and two loadable naming layers.
Counts below include regular instructions, early timeline instructions, and global names.
“Upstream / correspondence / neutral” distinguishes preserved source names, fork-owned naming correspondences, and unresolved neutral names.
Compiler-known signature coverage is not a list of instructions confirmed to execute in each game.

| Version | Regular signatures | Timeline signatures | Globals | zero318: upstream / correspondence / neutral | Priw8: upstream / correspondence / neutral |
| --- | ---: | ---: | ---: | ---: | ---: |
| TH06 | 136 | 13 | 25 | 174 / 0 / 0 | 0 / 85 / 89 |
| TH07 | 162 | 13 | 74 | 249 / 0 / 0 | 0 / 172 / 77 |
| TH08 | 185 | 17 | 101 | 301 / 0 / 2 | 271 / 0 / 32 |
| TH09 | 188 | 18 | 97 | 303 / 0 / 0 | 0 / 243 / 60 |
| TH095 | 185 | 18 | 84 | 244 / 0 / 43 | 0 / 189 / 98 |
| TH10 | 179 | 0 | 71 | 228 / 21 / 1 | 250 / 0 / 0 |
| TH103 | 192 | 0 | 79 | 270 / 0 / 1 | 0 / 228 / 43 |
| TH11 | 209 | 0 | 98 | 304 / 2 / 1 | 276 / 0 / 31 |
| TH12 | 278 | 0 | 92 | 291 / 0 / 79 | 315 / 1 / 54 |
| TH125 | 290 | 0 | 118 | 353 / 0 / 55 | 0 / 266 / 142 |
| TH128 | 296 | 0 | 92 | 0 / 270 / 118 | 333 / 0 / 55 |
| TH13 | 374 | 0 | 96 | 0 / 329 / 141 | 363 / 0 / 107 |
| TH14 | 383 | 0 | 96 | 0 / 341 / 138 | 382 / 0 / 97 |
| TH143 | 386 | 0 | 96 | 0 / 341 / 141 | 385 / 0 / 97 |
| TH15 | 389 | 0 | 97 | 380 / 0 / 106 | 388 / 0 / 98 |
| TH16 | 390 | 0 | 97 | 0 / 343 / 144 | 388 / 0 / 99 |
| TH165 | 398 | 0 | 97 | 0 / 340 / 155 | 397 / 0 / 98 |
| TH17 | 399 | 0 | 101 | 0 / 344 / 156 | 406 / 0 / 94 |
| TH18 | 402 | 0 | 103 | 391 / 0 / 114 | 407 / 0 / 98 |
| TH185 | 413 | 0 | 110 | 422 / 0 / 101 | 412 / 0 / 111 |
| TH19 | 429 | 0 | 108 | 427 / 0 / 110 | 0 / 304 / 233 |
| TH20 | 432 | 0 | 115 | 414 / 0 / 133 | 0 / 310 / 237 |

Source selection and every synthesized or unresolved name are recorded in [import-audit.json](import-audit.json).
The count table and [coverage.json](coverage.json) describe the initial import; native ECLM files remain the maintained data.

The following are explicitly outside this baseline: trial builds, TH06NC, ZECL/custom opcodes, and a claim of complete behavior documentation.
See [SOURCES.md](../SOURCES.md) for native signature choices, global-type conflicts, and licensing provenance.
