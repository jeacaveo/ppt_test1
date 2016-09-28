import os
from unittest import TestCase
from utils import data

class TestReadJsonFile(TestCase):
    """ Test all functions related to parsing a Json file. """

    def test_read_file(self):
        """
        Test function to get a file by it's location/name works properly,
        when provided with a valid file.

        """
        # Given
        file_location_name = os.path.join(os.getcwd(), "post.json")

        # When
        errors, loaded_file = data.get_file(file_location_name)

        # Then
        self.assertFalse(errors)
        self.assertTrue(loaded_file)
