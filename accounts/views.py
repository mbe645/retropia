from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically login after registration
            return redirect('accounts:profile_view', username=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:profile_view', username=user.username)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# User logout view
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# View for displaying a user's profile
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

# View for editing current user's profile
@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_view', username=request.user.username)  # ✅ Buraya düzeltme yapıldı
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})

