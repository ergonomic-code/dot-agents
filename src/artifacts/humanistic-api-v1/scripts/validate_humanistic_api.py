#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import NamedTuple


MARKDOWN_OPEN = "```text"
MARKDOWN_CLOSE = "```"
ASCIIDOC_MARKER = "[source,text]"
ASCIIDOC_FENCE = "----"
METHOD_RE = re.compile(r"Method (GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE) /\S+$")
DEFINITION_RE = re.compile(r"(Model|Enum) [A-Za-z_][A-Za-z0-9_.-]* =$", re.ASCII)
QUERY_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*=\{(.+)\}&?$")
FIELD_RE = re.compile(r'"[^"\n]+"\s*:\s*(.+?)(?:,)?(?:\s+//.*)?$')
HEADER_OR_PART_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*\s*:\s*(\S.*)$")
STATUS_RE = re.compile(r"[1-5][0-9]{2}(?:\s*,\s*[1-5][0-9]{2})*(?:\s+//.*)?$")
VARIANT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*(?:\s*\|)?$")
ENUM_ITEM_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*(?:\s+//.*)?$")
NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*", re.ASCII)
PRIMITIVES = {"String", "Number", "Boolean", "Binary", "Object"}


class SourceBlock(NamedTuple):
    line: int
    lines: list[str]


def _consume_type(value: str, position: int = 0) -> int | None:
    if value.startswith("Enum<", position):
        end = value.find(">", position + 5)
        if end == -1:
            return None
        names = value[position + 5 : end].split("|")
        if not names or any(NAME_RE.fullmatch(name) is None for name in names):
            return None
        position = end + 1
    elif value.startswith("<", position):
        end = value.find(">", position + 1)
        if end == -1:
            return None
        names = value[position + 1 : end].split("|")
        if not names or any(NAME_RE.fullmatch(name) is None for name in names):
            return None
        position = end + 1
    elif value.startswith("[", position):
        position = _consume_type(value, position + 1)
        if position is None or position >= len(value) or value[position] != "]":
            return None
        position += 1
    elif value.startswith("{", position):
        end = value.find("}", position + 1)
        if end == -1 or not value[position + 1 : end].strip():
            return None
        position = end + 1
    else:
        match = NAME_RE.match(value, position)
        if match is None or match.group() not in PRIMITIVES:
            return None
        position = match.end()
        if position < len(value) and value[position] == ":":
            refinement = NAME_RE.match(value, position + 1)
            if refinement is None:
                return None
            position = refinement.end()
    if position < len(value) and value[position] == "?":
        position += 1
    return position


def _is_type(value: str) -> bool:
    return _consume_type(value) == len(value)


def _is_body(value: str) -> bool:
    return value == "none" or _is_type(value)


def _strip_gutter(line: str) -> str:
    if line[:1] in {"+", "*", "x"}:
        return line[1:]
    return line


def extract_blocks(text: str) -> tuple[list[SourceBlock], list[str]]:
    lines = text.splitlines()
    blocks: list[SourceBlock] = []
    errors: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line == MARKDOWN_OPEN:
            start = index + 1
            index += 1
            content: list[str] = []
            while index < len(lines) and lines[index].strip() != MARKDOWN_CLOSE:
                content.append(lines[index])
                index += 1
            if index == len(lines):
                errors.append(f"line {start}: unclosed Markdown text fence")
                break
            blocks.append(SourceBlock(start + 1, content))
        elif line == ASCIIDOC_MARKER:
            if index + 1 >= len(lines) or lines[index + 1].strip() != ASCIIDOC_FENCE:
                errors.append(f"line {index + 1}: [source,text] must be followed by ----")
            else:
                start = index + 2
                index += 2
                content = []
                while index < len(lines) and lines[index].strip() != ASCIIDOC_FENCE:
                    content.append(lines[index])
                    index += 1
                if index == len(lines):
                    errors.append(f"line {start}: unclosed AsciiDoc text block")
                    break
                blocks.append(SourceBlock(start + 1, content))
        index += 1
    return blocks, errors


def _content_lines(block: SourceBlock) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    for offset, raw_line in enumerate(block.lines):
        normalized = _strip_gutter(raw_line).strip()
        if normalized:
            result.append((block.line + offset, normalized))
    return result


def _validate_rules(lines: list[tuple[int, str]], errors: list[str]) -> None:
    for index, (line_number, line) in enumerate(lines):
        if line != "Rules:":
            continue
        if index + 1 == len(lines) or not lines[index + 1][1].startswith("- "):
            errors.append(f"line {line_number}: Rules must contain at least one '- ' item")
        for child_line, child in lines[index + 1 :]:
            if not child.startswith("- "):
                errors.append(f"line {child_line}: only '- ' items are allowed after Rules:")


def validate_block(block: SourceBlock) -> list[str]:
    lines = _content_lines(block)
    if not lines:
        return [f"line {block.line}: empty API source block"]
    first_number, first = lines[0]
    errors: list[str] = []
    if METHOD_RE.fullmatch(first):
        _validate_endpoint(lines, errors)
    elif DEFINITION_RE.fullmatch(first):
        if first.startswith("Model "):
            _validate_model(lines, errors)
        else:
            _validate_enum(lines, errors)
    else:
        errors.append(
            f"line {first_number}: source block must start with Method, Model, or Enum"
        )
    _validate_rules(lines, errors)
    return errors


def _validate_endpoint(lines: list[tuple[int, str]], errors: list[str]) -> None:
    request_count = sum(line == ">" for _, line in lines)
    response_count = sum(line == "<" for _, line in lines)
    if request_count > 1:
        errors.append(f"line {lines[0][0]}: endpoint has more than one request marker")
    if response_count != 1:
        errors.append(f"line {lines[0][0]}: endpoint must have exactly one response marker")
    response_seen = False
    section: str | None = None
    status_seen = False
    multipart = False
    for line_number, line in lines[1:]:
        if line == "Rules:":
            break
        if line == ">":
            section = "request"
            continue
        if line == "<":
            response_seen = True
            section = "response"
            continue
        if line in {"Headers:", "Body:"}:
            section = line[:-1].lower()
            multipart = False
            continue
        if line == "multipart/form-data":
            multipart = True
            continue
        if line.startswith("- "):
            continue
        if not response_seen and section is None:
            match = QUERY_RE.fullmatch(line)
            if match is None or not _is_type(match.group(1)):
                errors.append(f"line {line_number}: invalid query parameter")
        elif response_seen and STATUS_RE.fullmatch(line):
            status_seen = True
            section = "response-body"
        elif section == "headers" or multipart:
            match = HEADER_OR_PART_RE.fullmatch(line)
            value = match.group(1) if match else ""
            quoted_header = section == "headers" and len(value) >= 2 and value[0] == value[-1] == '"'
            if match is None or not (quoted_header or _is_type(value)):
                errors.append(f"line {line_number}: invalid header or multipart part")
        elif section in {"body", "response-body"}:
            if not _is_body(line):
                errors.append(f"line {line_number}: invalid body type")
        else:
            errors.append(f"line {line_number}: unexpected endpoint line: {line}")
    if response_seen and not status_seen:
        errors.append(f"line {lines[0][0]}: response must contain at least one status")


def _validate_model(lines: list[tuple[int, str]], errors: list[str]) -> None:
    body = [(number, line) for number, line in lines[1:] if line != "Rules:" and not line.startswith("- ")]
    if not body:
        errors.append(f"line {lines[0][0]}: model has no body")
        return
    if body[0][1] == "{":
        if body[-1][1] != "}":
            errors.append(f"line {body[-1][0]}: model object must end with }}")
        for line_number, line in body[1:-1]:
            if line == "<...>":
                continue
            match = FIELD_RE.fullmatch(line)
            if match is None or not _is_type(match.group(1)):
                errors.append(f"line {line_number}: invalid model field")
    else:
        for line_number, line in body:
            if not VARIANT_RE.fullmatch(line):
                errors.append(f"line {line_number}: invalid sum-type variant")


def _validate_enum(lines: list[tuple[int, str]], errors: list[str]) -> None:
    items = [(number, line) for number, line in lines[1:] if line != "Rules:" and not line.startswith("- ")]
    if not items:
        errors.append(f"line {lines[0][0]}: enum has no items")
    for line_number, line in items:
        if not ENUM_ITEM_RE.fullmatch(line):
            errors.append(f"line {line_number}: invalid enum item")


def validate_document(text: str) -> list[str]:
    blocks, errors = extract_blocks(text)
    if not blocks and not errors:
        errors.append("document contains no text source blocks")
    for block in blocks:
        errors.extend(validate_block(block))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate humanistic-api/v1 source blocks.")
    parser.add_argument("artifact", type=Path, help="Markdown or AsciiDoc artifact path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_document(args.artifact.read_text(encoding="utf-8"))
    if errors:
        print("Validation failed.", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
