"""Tests for word_count."""

import pytest

from textutils.counting import word_count


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
