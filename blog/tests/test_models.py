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


class PostTestCase(TestCase):
    def setUp(self):
        # Authors
        self.author1 = models.Author.objects.create(name="J. Snow")
        self.author2 = models.Author.objects.create(name="S. Stark")

        # Tags
        self.tag1 = models.Tag.objects.create(name="cooking")
        self.tag2 = models.Tag.objects.create(name="sports")

        # Posts
        self.post1 = models.Post.objects.create(
            title="Post 1",
            description="This post has a description with ten words exatly "
                        "here. Everything else is not part of the summary.",
            author=self.author1)
        self.post2 = models.Post.objects.create(
            title="Post 2",
            description="Body for post 2",
            author=self.author2)
        self.post2.tags.add(self.tag1, self.tag2)

    def test_post_no_tags(self):
        """ Test post without tags can be created. """
        # Given
        post_title = "Post 1"

        # When
        post = models.Post.objects.get(title=post_title)

        # Then
        self.assertEqual(post, self.post1)
        self.assertEqual(post.title, post_title)
        self.assertEqual(post.tags.count(), 0)

    def test_post_tags(self):
        """ Test post with tags can be created. """
        # Given
        post_title = "Post 2"

        # When
        post = models.Post.objects.get(title=post_title)

        # Then
        self.assertEqual(post, self.post2)
        self.assertEqual(post.title, post_title)
        self.assertEqual(post.tags.count(), 2)

    def test_post_filter_id(self):
        """ Test filter of post by ID. """
        # Given
        post_id = 1

        # When
        post = models.Post.objects.get(id=post_id)

        # Then
        self.assertEqual(post, self.post1)
        self.assertEqual(post.id, post_id)

    def test_post_filter_author_name(self):
        """ Test filter of post by Author. """
        # Given
        author_name = self.author1.name

        # When
        post = models.Post.objects.filter(author__name=author_name).first()

        # Then
        self.assertEqual(post, self.post1)
        self.assertEqual(post.author.name, author_name)

    def test_post_filter_author(self):
        """ Test filter of post by Author object. """
        # Given
        author = self.author1

        # When
        post = models.Post.objects.filter(author=author).first()

        # Then
        self.assertEqual(post, self.post1)
        self.assertEqual(post.author, author)

    def test_post_tag_name_filter(self):
        """ Test filter of post by Tag name. """
        # Given
        tag_name = self.tag2.name

        # When
        post = models.Post.objects.filter(tags__name=tag_name).first()

        # Then
        self.assertEqual(post, self.post2)
        self.assertEqual(post.tags.all()[1].name, tag_name)

    def test_post_tag_filter(self):
        """ Test filter of post by Tag object. """
        # Given
        tag = self.tag2

        # When
        post = models.Post.objects.filter(tags=tag).first()

        # Then
        self.assertEqual(post, self.post2)
        self.assertEqual(post.tags.all()[1], tag)

    def test_post_summary(self):
        """ Test summary field returns only first 10 words of description. """
        # Given
        expected_summary = ("This post has a description with ten words "
                            "exatly here.")

        # When
        post = models.Post.objects.get(id=self.post1.id)

        # Then
        self.assertEqual(post.summary, expected_summary)
        self.assertNotEqual(post.description, post.summary)
