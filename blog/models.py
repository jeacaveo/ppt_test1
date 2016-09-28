from django.db import models
from utils.data import get_first_words_from_string


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def _get_frecuency(self):
        "Returns amount of Posts associated to each Tag."
        return Post.objects.filter(tags=self.id).count()

    frecuency = property(_get_frecuency)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def _get_summary(self):
        "Returns the first 10 words of the description."
        return get_first_words_from_string(self.description, 10)

    summary = property(_get_summary)

    def __str__(self):
        return self.title
