from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register_view, name='reg'),
    path('login', views.login_view, name='log'),
    path('logout', views.logout_view, name='lout'),
]