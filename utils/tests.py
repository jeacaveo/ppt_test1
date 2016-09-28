import os
from unittest import TestCase
from utils import data


class ReadJsonFileTestCase(TestCase):
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

    def test_nested_json_file(self):
        """
        Test function to get an object based on a JSON file,
        when provided with a valid file location.

        """
        # Given
        file_location_name = os.path.join(os.getcwd(), "posts.json")

        # When
        error, obj = data.get_json_from_file(file_location_name)

        # Then
        self.assertFalse(error)
        self.assertEqual(obj.get("posts")[0].get("id"), "1")

    def test_json_file_not_found_error(self):
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

    def test_json_format_file_error(self):
        """
        Test function to get an object based on a JSON file returns an error,
        when provided with an invalid JSON in the file.

        """
        # Given
        file_location_name = os.path.join(os.getcwd(), "README.md")

        # When
        error, loaded_file = data.get_json_from_file(file_location_name)

        # Then
        self.assertEqual(error, "Expecting value: line 1 column 1 (char 0)")
        self.assertFalse(loaded_file)


class WordCountTestCase(TestCase):
    """ Test all functions related to string parsing and counting. """

    def test_multiple_words_count(self):
        """
        Test function to get amount of words in a string with multiple words
        to work properly.

        """
        # Given
        text = "This text has five words."

        # When
        word_count = data.get_word_count(text)

        # Then
        self.assertEqual(word_count, 5)

    def test_single_word_count(self):
        """
        Test function to get amount of words in a string with a single word
        to work properly.

        """
        # Given
        text = "One."

        # When
        word_count = data.get_word_count(text)

        # Then
        self.assertEqual(word_count, 1)

    def test_no_words_count(self):
        """
        Test function to get amount of words in a string with no words
        to work properly.

        """
        # Given
        text = ""

        # When
        word_count = data.get_word_count(text)

        # Then
        self.assertEqual(word_count, 0)

    def test_get_first_words_from_string(self):
        """
        Test function to get first N words from a string, when the specified
        amount is lower than the word total.

        """
        # Given
        text = "This text has five words."

        # When
        first_words = data.get_first_words_from_string(text, 3)

        # Then
        self.assertEqual(first_words, "This text has")

    def test_get_first_words_from_string_same(self):
        """
        Test function to get first N words from a string, when the specified
        amount is the same as the word total.

        """
        # Given
        text = "This text has five words."

        # When
        first_words = data.get_first_words_from_string(text, 5)

        # Then
        self.assertEqual(first_words, text)

    def test_get_first_words_from_string_greater(self):
        """
        Test function to get first N words from a string, when the specified
        amount is greater than the word total.

        """
        # Given
        text = "One."

        # When
        first_words = data.get_first_words_from_string(text, 3)

        # Then
        self.assertEqual(first_words, "One.")

    def test_get_first_words_from_string_empty(self):
        """
        Test function to get first N words from a string, when the specified
        string is empty.

        """
        # Given
        text = ""

        # When
        first_words = data.get_first_words_from_string(text, 3)

        # Then
        self.assertEqual(first_words, "")
