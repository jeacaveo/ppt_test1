from django.core.urlresolvers import reverse
from django.test import TestCase
from blog import models


class PostViewsTests(TestCase):
    """ Test whether our post entries show up on the posts page. """

    def setUp(self):
        self.tag = models.Tag.objects.create(name="cooking")
        self.author = models.Author.objects.create(name="J. Snow")

        self.post1 = models.Post.objects.create(
            title="Post 1",
            description="Body for post 1",
            author=self.author)
        self.post1.tags.add(self.tag)

        self.post2 = models.Post.objects.create(
            title="Post 2",
            description="Body for post 2",
            author=self.author)

    def test_post_list(self):
        """ Test posts list endpoint returns expected information. """
        # Given
        url = reverse("post-list")

        # When
        response = self.client.get(url)

        # Then
        self.assertContains(response, self.post2.title)
        self.assertContains(response, self.post2.title)

    def test_post_detail(self):
        """
        Test posts details endpoint returns expected information for
        first post and no information from second post.

        """
        # Given
        url = reverse("post-detail", args=[self.post1.id])

        # When
        response = self.client.get(url)

        # Then
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.description)
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.tag.name)
        self.assertNotContains(response, self.post2.title)
        self.assertNotContains(response, self.post2.description)
