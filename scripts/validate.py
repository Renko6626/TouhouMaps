#!/usr/bin/env python3
"""Validate the maintained native ECLM layers; no downloads or generation."""

import argparse
import re
from pathlib import Path

VERSIONS = (6, 7, 8, 9, 95, 10, 103, 11, 12, 125, 128, 13, 14, 143,
            15, 16, 165, 17, 18, 185, 19, 20)
NAME_SECTIONS = {
    "ins_names": "ins_signatures",
    "timeline_ins_names": "timeline_ins_signatures",
    "gvar_names": "gvar_types",
}
KEYWORDS = set("anim ecli sub timeline var int float void inline return goto "
               "unless if else do while times switch case default break async "
               "global sin cos sqrt rad false true continue string loop".split())
# Native value types plus thecl's label, subroutine, and call-argument types.
# A single trailing *type consumes the remaining parameters (value.c).
SIGNATURE = re.compile(r"[bcdfusUSCzmnNTotxDH]*(?:\*[bcdfusUSCzmnNTotxDH])?")


def read_map(path: Path, allowed: set[str]) -> dict[str, dict[int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "!eclmap":
        raise ValueError(f"{path}: expected !eclmap header")
    sections: dict[str, dict[int, str]] = {}
    section = ""
    for number, raw in enumerate(lines[1:], 2):
        if len(raw.encode("utf-8")) >= 511:
            raise ValueError(f"{path}:{number}: exceeds thecl's line buffer")
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("!"):
            section = line[1:]
            if section not in allowed or section in sections:
                raise ValueError(f"{path}:{number}: invalid/repeated section {section}")
            sections[section] = {}
            continue
        match = re.fullmatch(r"(-?\d+)(?:\s+(\S+))?", line)
        if not section or not match:
            raise ValueError(f"{path}:{number}: invalid mapping line")
        key, value = int(match[1]), match[2] or ""
        if key in sections[section]:
            raise ValueError(f"{path}:{number}: duplicate key {key}")
        if section != "gvar_types" and section != "gvar_names" and key < 0:
            raise ValueError(f"{path}:{number}: negative instruction opcode")
        if section in NAME_SECTIONS:
            if (not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value)
                    or value in KEYWORDS or value.startswith("ins_")):
                raise ValueError(f"{path}:{number}: invalid mnemonic {value!r}")
            if value in sections[section].values():
                raise ValueError(f"{path}:{number}: ambiguous mnemonic {value!r}")
        elif section == "gvar_types":
            if value not in ("$", "%", "?"):
                raise ValueError(f"{path}:{number}: invalid global type {value!r}")
        elif not SIGNATURE.fullmatch(value):
            raise ValueError(f"{path}:{number}: non-native signature {value!r}")
        sections[section][key] = value
    return sections


def validate(root: Path) -> None:
    expected = {("th095" if v == 95 else f"th{v:02}") + ".eclm"
                for v in VERSIONS}
    for directory in (root / "common", root / "names/zero318", root / "names/priw8"):
        found = {path.name for path in directory.glob("*.eclm")}
        if found != expected:
            raise ValueError(f"{directory}: missing {sorted(expected-found)}, "
                             f"unexpected {sorted(found-expected)}")
    for name in sorted(expected):
        common = read_map(root / "common" / name, set(NAME_SECTIONS.values()))
        if not common.get("ins_signatures"):
            raise ValueError(f"{name}: empty instruction signature coverage")
        for style in ("zero318", "priw8"):
            names = read_map(root / "names" / style / name, set(NAME_SECTIONS))
            for section, shared in NAME_SECTIONS.items():
                actual = set(names.get(section, {}))
                wanted = set(common.get(shared, {}))
                if actual != wanted:
                    raise ValueError(f"{style}/{name}/{section}: "
                                     f"missing {sorted(wanted-actual)}, "
                                     f"extra {sorted(actual-wanted)}")
    print(f"OK: {len(expected)} common maps, {len(expected)*2} name profiles; "
          "native sections, coverage, identifiers, and global types are consistent.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate(args.root)
    except (OSError, ValueError) as error:
        parser.exit(1, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()
