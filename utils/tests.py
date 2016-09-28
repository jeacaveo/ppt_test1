import os
from unittest import TestCase
from utils import data

class TestReadJsonFile(TestCase):
    """ Test all functions related to parsing a Json file. """

    def test_read_file(self):
        """
        Test function to get a file by it's location/name works properly,
        when provided with a valid file location.

        """
        # Given
        file_location_name = os.path.join(os.getcwd(), "post.json")

        # When
        errors, loaded_file = data.get_file(file_location_name)

        # Then
        self.assertFalse(errors)
        self.assertTrue(loaded_file)

    def test_read_file_error(self):
        """
        Test function to get a file by it's location/name returns an error,
        when provided with an invalid file location.

        """
        # Given
        file_location_name = "bad_location_name"

        # When
        error, loaded_file = data.get_file(file_location_name)

        # Then
        self.assertEqual(error, "No such file or directory")
        self.assertFalse(loaded_file)
