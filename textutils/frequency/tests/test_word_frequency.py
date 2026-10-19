"""Tests for word_frequency."""

import pytest

from textutils.frequency import word_frequency


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
