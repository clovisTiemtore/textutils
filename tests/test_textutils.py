"""Tests for the public textutils API."""

import pytest

from textutils import (
    capitalize_words,
    character_count,
    reverse,
    snake_case,
    word_count,
    word_frequency,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("hello world", "Hello World"),
        ("  hello\tWORLD  ", "  Hello\tWorld  "),
        ("they're co-operating", "They'Re Co-Operating"),
    ],
)
def test_capitalize_words(text: str, expected: str) -> None:
    assert capitalize_words(text) == expected


@pytest.mark.parametrize(
    ("text", "include_spaces", "expected"),
    [
        ("", True, 0),
        ("hello world", True, 11),
        ("hello world", False, 10),
        ("a  b", False, 2),
        ("a\tb\nc", False, 5),
        ("café ☕", True, 6),
    ],
)
def test_character_count(
    text: str,
    include_spaces: bool,
    expected: int,
) -> None:
    assert character_count(text, include_spaces) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        (" \t\n ", 0),
        ("one two three", 3),
        ("one,\ttwo\nthree!", 3),
        ("café 東京", 2),
    ],
)
def test_word_count(text: str, expected: int) -> None:
    assert word_count(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("text", "txet"),
        ("a b\n", "\nb a"),
        ("café", "éfac"),
    ],
)
def test_reverse(text: str, expected: str) -> None:
    assert reverse(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("hello world", "hello_world"),
        ("  hello\tOpen\nSource  ", "hello_Open_Source"),
        ("already_snake_case", "already_snake_case"),
        ("café 東京", "café_東京"),
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", {}),
        ("!!! ... ,,,", {}),
        ("The AND a to", {}),
        ("The cat and the dog. The cat!", {"cat": 2, "dog": 1}),
        ("pear apple banana", {"apple": 1, "banana": 1, "pear": 1}),
        ("CAFÉ café Ελληνικά", {"café": 2, "ελληνικά": 1}),
        ("one,two;three", {"one": 1, "three": 1, "two": 1}),
        ("can't re-enter", {"can": 1, "enter": 1, "re": 1, "t": 1}),
    ],
)
def test_word_frequency(text: str, expected: dict[str, int]) -> None:
    assert word_frequency(text) == expected


@pytest.mark.parametrize(
    "separator",
    [
        "'",
        "`",
        "‘",
        "’",
        "ʼ",
        "-",
        "‐",
        "‑",
        "‒",
        "–",
        "—",
        "―",
    ],
)
def test_word_frequency_splits_on_apostrophes_and_hyphens(
    separator: str,
) -> None:
    assert word_frequency(f"alpha{separator}beta") == {"alpha": 1, "beta": 1}


def test_word_frequency_rejects_non_string_input() -> None:
    with pytest.raises(TypeError, match="text must be a string"):
        word_frequency(None)  # type: ignore[arg-type]


def test_public_api_exports_all_operations() -> None:
    assert callable(capitalize_words)
    assert callable(character_count)
    assert callable(reverse)
    assert callable(snake_case)
    assert callable(word_count)
    assert callable(word_frequency)
