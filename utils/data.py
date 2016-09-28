""" Module in charge of data manipulation entities. """
from json import load


def get_json_from_file(file_location_name):
    """
    Get an object representation of a JSON file object.

    Parameters:
        file_obj: File object
            JSON file object.

    Returns:
        (Error (str), JSON python object representation or None)

    """
    try:
        with open(file_location_name) as file_obj:
            return "", load(file_obj)
    except OSError as e:
        return e.strerror, None
    except ValueError as e:
        return e.args[0], None


def get_word_count(text):
    """
    Get amount of words in a string.

    Parameters:
        text: str
            String to be evaluated.

    Returns:
        int

    """
    return len(text.split(" ")) if text else 0


def get_first_words_from_string(text, amount):
    """
    Get the first N amount of words in a string.

    Parameters:
        text: str
            String to be evaluated.
        amount: int
            Amount of words to get from string.

    Returns:
        str

    """
    return " ".join(text.split(" ")[:amount])
