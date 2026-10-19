"""Tests for character_count."""

import pytest

from textutils.counting import character_count


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
