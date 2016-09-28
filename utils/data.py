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
