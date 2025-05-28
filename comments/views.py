from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from blog.models import BlogPost
from cards.models import Card
from .models import Comment

def index(request):
    return HttpResponse("Welcome to the Comments section.")

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        target_type = request.POST.get('target_type')
        target_id = request.POST.get('target_id')
        if form.is_valid() and target_type in ['blog', 'card']:
            comment = form.save(commit=False)
            comment.user = request.user
            if target_type == 'blog':
                comment.blog_post = get_object_or_404(BlogPost, pk=target_id)
                redirect_url = comment.blog_post.get_absolute_url() if hasattr(comment.blog_post, 'get_absolute_url') else '/'
            elif target_type == 'card':
                comment.card = get_object_or_404(Card, pk=target_id)
                redirect_url = comment.card.get_absolute_url() if hasattr(comment.card, 'get_absolute_url') else '/'
            comment.save()
            return redirect(redirect_url)
    return redirect('/')

@login_required
def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment_list.html', {'comments': comments})
