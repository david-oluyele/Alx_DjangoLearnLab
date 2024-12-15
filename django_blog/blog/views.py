from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # Create a form instance with the POST data and current profile instance
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('profile')  # Redirect to the profile page to reflect changes
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'form': form})
