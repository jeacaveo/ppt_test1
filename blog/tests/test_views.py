from django.core.urlresolvers import reverse
from django.test import TestCase
from blog import models


class PostViewsTests(TestCase):
    """ Test whether our post entries show up on the posts page. """

    def setUp(self):
        self.author = models.Author.objects.create(name="J. Snow")
        self.post1 = models.Post.objects.create(
            title="Post 1",
            description="Body for post 1",
            author=self.author)
        self.post2 = models.Post.objects.create(
            title="Post 2",
            description="Body for post 2",
            author=self.author)

    def test_post_list(self):
        # Given (two pre-existing Posts)
        url = reverse("post-list")

        # When
        response = self.client.get(url)

        # Then
        self.assertContains(response, "Post 1")
        self.assertContains(response, "Post 2")
