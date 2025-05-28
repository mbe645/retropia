from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Page

def index(request):
    return HttpResponse("Welcome to the Pages section.")

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})
