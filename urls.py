from django.urls import path
from . import views

#Name of the application and its url pathways.

app_name = 'public'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('home/', views.home_view, name = 'home'),
    path('about/', views.about_view, name = 'about'),
    path('contact/', views.contact_view, name = 'contact'),
    path('login/', views.login_view, name = 'login')
]