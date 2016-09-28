import os
from unittest import TestCase
from utils import data

class TestReadJsonFile(TestCase):
    """ Test all functions related to parsing a Json file. """

    def test_json_file(self):
        """
        Test function to get an object based on a JSON file,
        when provided with a valid file location.

        """
        # Given
        file_location_name = os.path.join(os.getcwd(), "post.json")

        # When
        error, obj = data.get_json_from_file(file_location_name)

        # Then
        self.assertFalse(error)
        self.assertEqual(obj.get("id"), "1")

    def test_json_file_error(self):
        """
        Test function to get an object based on a JSON file returns an error,
        when provided with an invalid file location.

        """
        # Given
        file_location_name = "bad_location_name"

        # When
        error, loaded_file = data.get_json_from_file(file_location_name)

        # Then
        self.assertEqual(error, "No such file or directory")
        self.assertFalse(loaded_file)
