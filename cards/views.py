from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required  # GİRİŞ KONTROLÜ
from cards.models import Card
from favorites.models import Favorite
from django.contrib.auth.models import User
from comments.models import Comment
from comments.forms import CommentForm
from .forms import CardForm
from django.shortcuts import redirect

@login_required
def index(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, card=card).exists()
    comments = card.comments.all().order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.card = card
            comment.save()
            return redirect('cards:card-detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'cards/card_detail.html', {
        'card': card,
        'is_favorited': is_favorited,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:cards-home')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})
