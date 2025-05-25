from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register_view, name='reg'),
    path('login', views.login_view, name='log'),
    path('logout', views.logout_view, name='lout'),
    path('showrasxod', views.show_rasxod, name='showr'),
    path('showdoxod', views.show_doxod, name='showd'),
    path('addrasxod',views.add_rasxod, name='addr')
]