# textutils

A lightweight Python library for common text-processing operations.

## Features

- `word_count(text)`: Count the number of words in a text.
- `character_count(text, include_spaces=True)`: Count characters with optional space inclusion.
- `reverse(text)`: Reverse the characters in a text.
- `capitalize_words(text)`: Capitalize the first letter of each word.
- `snake_case(text)`: Convert a text to snake case.
- `word_frequency(text)`: Count words after punctuation and stop-word filtering.

## Installation

Create and activate a virtual environment, then install the package:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install .
```

To install it in editable mode with the development and testing tools:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```python
from textutils import word_count

count = word_count("Hello Open Source!")
print(count)
```

## Testing

Run the test suite and display line and branch coverage with:

```bash
python -m pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.