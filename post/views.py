from django.shortcuts import render # type: ignore
from django.views.generic import ListView,DeleteView # type: ignore
from .models import Post
# Create your views here.

class PostsShow(ListView):
    model = Post
    template_name = 'index.html'


class PostOpen(DeleteView):
    model = Post
    template_name = 'blog_detail.html'