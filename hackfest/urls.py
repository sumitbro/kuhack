from django.urls import path
from .views import DonorListView, DonorDetailView, BloodBankListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('donor', DonorListView.as_view(), name='Donor'),
    path('donor/<int:pk>/', DonorDetailView.as_view(), name='donor_detail'),

    path('blood_bank', BloodBankListView.as_view(), name='BloodBank'),
    path('create_donor', views.create_donor, name='create_donor')
    
    



]
