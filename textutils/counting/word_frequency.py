import string


_STOP_WORDS = {"the", "and", "a", "to"}


def word_frequency(text: str) -> dict[str, int]:
    """Count word frequencies after filtering common stop words.

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    dict[str, int]
        A dictionary mapping each word to its frequency, sorted by
        decreasing frequency and alphabetically when frequencies are equal.

    Raises
    ------
    TypeError
        If ``text`` is not a string.

    Examples
    --------
    >>> word_frequency("The cat and the dog. The cat!")
    {'cat': 2, 'dog': 1}
    >>> word_frequency("!!!")
    {}
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return {}

    lowercase_text = text.lower()
    apostrophe_characters = {
        "'",
        "`",
        "‘",
        "’",
        "ʼ",
    }
    hyphen_characters = {
        "-",
        "‐",
        "‑",
        "‒",
        "–",
        "—",
        "―",
    }

    characters_without_punctuation: list[str] = []
    for character in lowercase_text:
        if character.isspace():
            characters_without_punctuation.append(" ")
            continue

        if character in apostrophe_characters:
            characters_without_punctuation.append(" ")
            continue

        if character in hyphen_characters:
            characters_without_punctuation.append(" ")
            continue

        if character in string.punctuation:
            characters_without_punctuation.append(" ")
            continue

        characters_without_punctuation.append(character)

    cleaned_text = "".join(characters_without_punctuation)
    normalized_text = " ".join(cleaned_text.split())

    if not normalized_text:
        return {}

    individual_words = normalized_text.split(" ")
    filtered_words: list[str] = []

    for word in individual_words:
        if not word:
            continue

        if word in _STOP_WORDS:
            continue

        filtered_words.append(word)

    if not filtered_words:
        return {}

    word_counts: dict[str, int] = {}
    for word in filtered_words:
        current_count = word_counts.get(word, 0)

        if current_count == 0:
            word_counts[word] = 1
        else:
            word_counts[word] = current_count + 1

    count_items = list(word_counts.items())
    sorted_count_items = sorted(
        count_items,
        key=lambda item: (-item[1], item[0]),
    )

    sorted_frequencies: dict[str, int] = {}
    for word, count in sorted_count_items:
        sorted_frequencies[word] = count

    return sorted_frequencies
