from django.urls import path
from . import views

urlpatterns = [
    path(r'register', views.register, name='login_register'),
    path(r'register/success', views.register_success, name='login_register_success'),
]
