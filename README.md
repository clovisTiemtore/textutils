# textutils

A lightweight Python library providing simple utilities for common
text-processing operations.

Requires Python 3.12 or later.

## Features

- `word_count(text)`: Count the number of words in a text.
- `character_count(text, include_spaces=True)`: Count characters, optionally
  excluding spaces.
- `reverse(text)`: Reverse the characters in a text.
- `capitalize_words(text)`: Capitalize each word in a text.
- `snake_case(text)`: Convert whitespace-separated words to snake case.
- `word_frequency(text)`: Count normalized words after punctuation and common
  stop-word filtering.

## Installation

The first release is being prepared. Once it is published, install the package
from PyPI with:

```console
python -m pip install textutils-clovistiemtore
```

To install the project locally in editable mode with its development tools:

```console
python -m pip install -e ".[dev]"
python -m pip install pre-commit
```

## Usage

```python
from textutils import (
    capitalize_words,
    character_count,
    reverse,
    snake_case,
    word_count,
    word_frequency,
)

print(word_count("Hello Open Source!"))
print(character_count("Hello Open Source!", include_spaces=False))
print(reverse("Hello Open Source!"))
print(capitalize_words("hello open source!"))
print(snake_case("Hello Open Source!"))
print(word_frequency("Python is great. Python is simple."))
```

## Testing

Run the test suite with line and branch coverage:

```console
python -m pytest
```

Run the formatting, lint, and pre-commit checks:

```console
python -m black --check .
python -m ruff check .
pre-commit run --all-files
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for more details.
