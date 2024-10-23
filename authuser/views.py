from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegisterForm
from django.db import transaction
from dashboaed.models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            return redirect("login")
    else:
        form = UserRegisterForm()

    context = {'registerform': form}
    return render(request, 'accounts/register.html', context=context)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Welcome back!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid login credentials. Please try again.')
        return super().form_invalid(form)
    
def profile_view(request):
    return render(request, 'accounts/profile.html')