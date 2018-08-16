from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'register/success', views.register_success, name='login_register_success'),
    path(r'register', views.register, name='login_register'),
    path(r'login/', auth_views.login, name='login'),
    path(r'logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]
