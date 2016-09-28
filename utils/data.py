""" Module in charge of data manipulation entities. """

def get_file(file_location_name):
    """
    Gets a file object based on file_location.

    Parameters:
        file_location_name: str
            Full path and name of file to load.

    Returns:
        Error (str), File object

    """
    file_obj = open(file_location_name)
    return "", file_obj
