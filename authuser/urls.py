from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import register,profile_view
from dashboaed.views import homepage
urlpatterns = [
    path('', homepage, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/register/', register, name='register'), #User registration
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes the login URL pattern
]
