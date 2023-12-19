# urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from notes.views import RegisterView  # Добавьте этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('notes/', include('notes.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', RedirectView.as_view(url='login/', permanent=True), name='index'),

]
