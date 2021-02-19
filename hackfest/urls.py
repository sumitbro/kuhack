from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('donner', views.donner, name='donner'),
    path('bloodbank', views.bloodbank, name='bloodbank'),
    path('create_donor', views.create_donor, name='create_donor')
    
    



]
