"""Tests for reverse."""

import pytest

from textutils.transform import reverse


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
