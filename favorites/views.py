from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cards.models import Card
from .models import Favorite
from games.models import Game
from blog.models import BlogPost

def index(request):
    return HttpResponse("Welcome to the Favorites section.")

@login_required
def toggle_favorite(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, card=card)
    if not created:
        favorite.delete()
    # Kart detay sayfan yoksa ana sayfaya yönlendiriyorum, detay view eklenirse oraya yönlendirebiliriz
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user, card__isnull=False)
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})

@login_required
def toggle_favorite_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, game=game)
    if not created:
        favorite.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def toggle_favorite_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, blog=blog)
    if not created:
        favorite.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def favorite_games_list(request):
    favorites = Favorite.objects.filter(user=request.user, game__isnull=False)
    return render(request, 'favorites/favorite_games_list.html', {'favorites': favorites})

@login_required
def favorite_blogs_list(request):
    favorites = Favorite.objects.filter(user=request.user, blog__isnull=False)
    return render(request, 'favorites/favorite_blogs_list.html', {'favorites': favorites})
