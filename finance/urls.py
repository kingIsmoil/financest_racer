from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register_view, name='reg'),
    path('login', views.login_view, name='log'),
    path('logout', views.logout_view, name='lout'),
    path('show', views.get_dr, name='dr'),

    path('adddoxod', views.add_doxod, name='addd'),
    path('showdoxod', views.show_doxod, name='showd'),
    path('updatedoxod/<int:id>/', views.update_doxod, name='updd'),
    path('deletedoxod/<int:id>/', views.delete_doxod, name='deld'),

    path('addrasxod', views.add_rasxod, name='addr'),
    path('showrasxod', views.show_rasxod, name='showr'),
    path('updaterasxod/<int:id>/', views.update_rasxod, name='updr'),
    path('deleterasxod/<int:id>/', views.delete_rasxod, name='delr'),
]
