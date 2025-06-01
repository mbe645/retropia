from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BlogPost
from .forms import BlogPostForm, BlogCommentForm
from favorites.models import Favorite

def index(request):
    return render(request, 'blog/index.html')

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    favorited_blog_ids = set()
    if request.user.is_authenticated:
        favorited_blog_ids = set(Favorite.objects.filter(user=request.user, blog__isnull=False).values_list('blog_id', flat=True))
    return render(request, 'blog/blog_list.html', {'posts': posts, 'favorited_blog_ids': favorited_blog_ids})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, blog=post).exists()
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = post
            comment.save()
            return redirect('blog:blog-detail', pk=pk)
    else:
        form = BlogCommentForm()
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'form': form,
        'comments': comments,
        'is_favorited': is_favorited,
    })

@login_required
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            return redirect('blog:blog-detail', pk=blogpost.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpost_form.html', {'form': form})

@login_required
def edit_blogpost(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    if blogpost.author != request.user:
        return HttpResponseForbidden('You are not allowed to edit this post.')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blogpost)
        if form.is_valid():
            form.save()
            return redirect('blog:blog-detail', pk=pk)
    else:
        form = BlogPostForm(instance=blogpost)
    
    return render(request, 'blog/blogpost_form.html', {
        'form': form,
        'edit_mode': True
    })
