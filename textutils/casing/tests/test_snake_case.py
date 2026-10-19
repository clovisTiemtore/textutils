"""Tests for snake_case."""

import pytest

from textutils.casing import snake_case


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
