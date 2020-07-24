from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreatePost
from .models import Post, Author

USER = get_user_model()


def home(request):
    bio = Author.objects.values('bio')

    return render(request, 'blog/index.html', {'bio': bio})


def post(request):
    post = Post.objects.all()
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
    post = Post.objects.get(slug=title)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required()
def new_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.email = request.user
            post.save()
            return redirect('home')
    else:
        form = CreatePost()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required()
def post_update(request, title):
    obj = get_object_or_404(Post, slug=title)
    form = CreatePost(request.POST or None, request.FILES or None, instance=obj)
    post = Post.objects.get(slug=title)
    if request.user != post.email:
        return redirect('home')
    else:
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('home')
        template_name = 'blog/add_post.html'
        context = {"title": f"Update {obj.title}", "form": form}
        return render(request, template_name, context)


@login_required
def post_delete(request, title):
    obj = get_object_or_404(Post, slug=title)
    template_name = 'blog/delete.html'
    post = Post.objects.get(slug=title)
    if request.user != post.email:
        return redirect('home')
    else:
        if request.method == 'POST':
            obj.delete()
            return redirect('home')
        context = {"object": obj}
        return render(request, template_name, context)
