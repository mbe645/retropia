from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cards.models import Card
from .models import Favorite

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
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})
