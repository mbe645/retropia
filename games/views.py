from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import GameForm, GameCommentForm
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Welcome to the Games section.")

@login_required
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    comments = game.comments.all()
    if request.method == 'POST':
        form = GameCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = game
            comment.save()
            return redirect('games:game-detail', pk=pk)
    else:
        form = GameCommentForm()
    return render(request, 'games/game_detail.html', {
        'game': game,
        'form': form,
        'comments': comments
    })

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('games:games-home')
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', {'form': form})
