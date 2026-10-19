"""Tests for capitalize_words."""

import pytest

from textutils import (
    __all__ as public_api,
)
from textutils import (
    capitalize_words as public_capitalize_words,
)
from textutils import (
    character_count,
    reverse,
    snake_case,
    word_count,
    word_frequency,
)
from textutils.casing import capitalize_words


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


def test_public_api_exports_all_operations() -> None:
    assert public_api == [
        "capitalize_words",
        "character_count",
        "reverse",
        "snake_case",
        "word_count",
        "word_frequency",
    ]
    assert callable(public_capitalize_words)
    assert callable(character_count)
    assert callable(reverse)
    assert callable(snake_case)
    assert callable(word_count)
    assert callable(word_frequency)
