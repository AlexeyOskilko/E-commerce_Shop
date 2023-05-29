from django.views import generic
from .models import Post
from django.shortcuts import render
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-2.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# Create your views here.
