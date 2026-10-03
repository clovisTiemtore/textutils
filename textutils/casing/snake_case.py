def snake_case(text: str) -> str:
    """Convert a given text to snake case.

    Parameters
    ----------
    text : str
        The input text to convert.

    Returns
    -------
    str
        The text converted to snake case.
    """
    return "_".join(text.split())