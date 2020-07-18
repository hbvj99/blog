# from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Blog


def home(request):
    return render(request, 'blog/index.html')


def post(request):
    post = Blog.objects.all()
    post_search = request.GET.get("q")

    if post_search:
        post = post.filter(
            Q(title__icontains=post_search) |
            Q(description__icontains=post_search)
        ).distinct()

    paginator = Paginator(post, 3)

    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'blog/post.html', {'post': post})


def post_detail(request, title):
    post = Blog.objects.get(slug=title)
    return render(request, 'blog/post_detail.html', {'post': post})
