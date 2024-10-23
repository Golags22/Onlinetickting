from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import admin_view, create_event, edit_event, delete_event, homepage 
from django.contrib.auth import views as auth_views  # Import built-in auth views

urlpatterns = [
    path('', homepage, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes logout and password reset views
    path('accounts/admin_dashboard/', admin_view, name='dashboard'),
    path('admin_dashboard/create_event', create_event, name='create_event'),
    path('admin_dashboard/edit/<int:event_id>/', edit_event, name='edit_event'),
    path('admin_dashboard/delete/<int:event_id>/', delete_event, name='delete_event'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
