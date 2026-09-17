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