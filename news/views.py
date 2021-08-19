from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_created'] = datetime.utcnow()

        return context


class PostDetailedView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'
    queryset = Post.objects.all()
