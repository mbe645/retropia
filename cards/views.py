from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required  # GİRİŞ KONTROLÜ
from cards.models import Card
from favorites.models import Favorite
from django.contrib.auth.models import User
from comments.models import Comment
from comments.forms import CommentForm

@login_required
def index(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, card=card).exists()
    comments = card.comments.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'cards/card_detail.html', {
        'card': card,
        'is_favorited': is_favorited,
        'comments': comments,
        'comment_form': comment_form
    })
