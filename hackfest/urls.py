from django.urls import path
from .views import DonorListView, DonorDetailView, BloodBankListView, home, profile, create_donor, search

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile, name='profile'),
    path('donor', DonorListView.as_view(), name='Donor'),
    path('donor/<int:pk>/', DonorDetailView.as_view(), name='donor_detail'),

    path('blood_bank', BloodBankListView.as_view(), name='BloodBank'),
    path('create_donor', create_donor, name='create_donor'),
    path('search/', search, name='search')
    # path('search/', SearchView.as_view(), name='search')
    
    



]
