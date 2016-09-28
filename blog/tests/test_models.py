from django.test import TestCase
from blog import models


class AuthorTestCase(TestCase):
    def setUp(self):
        models.Author.objects.create(name="J. Snow")
        models.Author.objects.create(name="S. Stark")

    def test_author_object(self):
        """ Test proper creation of Authors in database. """
        # Given
        author_count = models.Author.objects.count()
        author_name = "J. Snow"

        # When
        author = models.Author.objects.get(name=author_name)
        not_author = models.Author.objects.filter(name="not_author").first()

        # Then
        self.assertEqual(author_count, 2)
        self.assertEqual(author.name, author_name)
        self.assertFalse(not_author)


class TagTestCase(TestCase):
    def setUp(self):
        models.Tag.objects.create(name="cooking")
        models.Tag.objects.create(name="sports")

    def test_author_object(self):
        """ Test proper creation of Tags in database. """
        # Given
        tag_count = models.Tag.objects.count()
        tag_name = "cooking"

        # When
        tag = models.Tag.objects.get(name=tag_name)
        not_tag = models.Tag.objects.filter(name="not_tag").first()

        # Then
        self.assertEqual(tag_count, 2)
        self.assertEqual(tag.name, tag_name)
        self.assertFalse(not_tag)
