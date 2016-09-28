from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog import models


class PostListView(ListView):
    """ List view for Posts. """
    model = models.Post


class PostDetailView(DetailView):
    """ Detail view for Posts. """
    model = models.Post
