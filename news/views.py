from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.shortcuts import render


# Main page where all posts are listed
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_created'] = datetime.utcnow()

        return context


# Search page with filters
class PostSearchView(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 20
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class PostDetailedView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/search'
