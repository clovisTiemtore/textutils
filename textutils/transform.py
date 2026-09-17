def word_count(text: str) -> int:
    """Count the number of words in a given text.

    Parameters
    ----------
    text : str
        The input text to analyze.

    Returns
    -------
    int
        The number of words in the text.
    """
    return len(text.split())

def character_count(text: str) -> int:
    """Count the number of characters in a given text.

    Parameters
    ----------
    text : str
        The input text to analyze.

    Returns
    -------
    int
        The number of characters in the text.
    """
    return len(text)

def reverse(text: str) -> str:
    """Reverse a given text.

    Parameters
    ----------
    text : str
        The input text to reverse.

    Returns
    -------
    str
        The reversed text.
    """
    return text[::-1]

def capitalize_words(text: str) -> str:
    """Capitalize each word in a given text.

    Parameters
    ----------
    text : str
        The input text to capitalize.

    Returns
    -------
    str
        The text with capitalized words.
    """
    return text.title()