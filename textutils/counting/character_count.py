def character_count(text: str, include_spaces: bool = True) -> int:
    """Count the number of characters in a given text.

    Parameters
    ----------
    text : str
        The input text to analyze.
    include_spaces : bool, optional
        Whether to include spaces in the count (default is True).

    Returns
    -------
    int
        The number of characters in the text.
    """
    if not include_spaces:
        return len(text.replace(" ", ""))
    return len(text)