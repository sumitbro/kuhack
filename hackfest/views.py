from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Donor, BloodBank


# Create your views here.

def home(request):
    return render(request, 'index.html')
    
    
def profile(request):
    return render(request, 'profile.html')
    

# def donner(request):
#     return render(request, 'donner.html')

class  DonorListView(ListView):
    model= Donor
    template_name='donor.html'
    context_object_name='data1'
    # ordering= ['-date_posted']
    # paginate_by=3


class  DonorDetailView(DetailView):
     model= Donor
     template_name='detail_donor.html'

class BloodBankListView(ListView):
    model= BloodBank
    template_name= 'blood_bank.html'
    context_object_name= 'data2'


def create_donor(request):
      if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        contact= request.POST['contact']
        dob= request.POST['dob']
        blood= request.POST.get('blood')
        district= request.POST['district']
        city= request.POST['city']
        ward= request.POST['ward']
        # gender= request.POST.get['gender']

        data=Donor(first_name=first_name, last_name=last_name,contact=contact, dob=dob, blood=blood, district=district, city=city, ward=ward)
        data.save()
        print("data saved")
        return redirect('/')
      else:
          return render(request, 'create_donor.html')
        




    


    