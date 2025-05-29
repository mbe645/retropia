from django import forms
from .models import Game, GameComment

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'platform', 'release_year']

class GameCommentForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ['content'] 