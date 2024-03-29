from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.registrationPage, name = 'register'),
    path('login', views.loginPage, name = 'login'),
    path('logout', views.logoutPage, name = 'logout'),

    path('settings', views.userSettingsPage, name="settings"),   

    path('upload-file/<str:id>', views.upload_view),
]