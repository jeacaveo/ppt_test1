from django.views.generic.list import ListView
from blog import models


class PostListView(ListView):
    model = models.Post
