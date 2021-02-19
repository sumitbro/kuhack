from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Donor

# Create your views here.

def home(request):
    return render(request, 'index.html')
    
    
def profile(request):
    return render(request, 'profile.html')
    

def donner(request):
    return render(request, 'donner.html')

def bloodbank(request):
    return render(request, 'bloodbank.html')

def create_donor(request):
      if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        contact= request.POST['contact']
        dob= request.POST['dob']
        district= request.POST['district']
        city= request.POST['city']
        ward= request.POST['ward']
        # gender= request.POST['gender']

        data=Donor(first_name=first_name, last_name=last_name,contact=contact, dob=dob, district=district, city=city, ward=ward)
        data.save()
        print("data saved")
        return redirect('/')
      else:
          return render(request, 'create_donor.html')
        




    


    