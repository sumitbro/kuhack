from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Donor, BloodBank
from django.contrib.auth.decorators import login_required

from .models import Donor

# Create your views here.

def home(request):
    return render(request, 'home.html', {'GROUP': Donor.BLOOD_GROUP})
    
    
def profile(request):
    return render(request, 'profile.html')

def search(request):
    # print(dir(request.GET))
    # print(request.GET.get('blood'))
    blood_group = request.GET.get('blood')
    data = Donor.objects.filter(blood=blood_group)
    # print(Donor.objects.all())
    # print(data)
    return render(request, 'donor.html', {'data1': data})

# class SearchView(ListView):
#     model = Donor
#     template_name = 'donor.html'

#     def get_queryset(self, *args, **kwargs):
#         # request = self.request
#         print(args, kwargs)
#         return Donor.objects.all()
    

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

@login_required(login_url="/accounts/login" )
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
        gender= request.POST['gender']

        data=Donor(first_name=first_name, last_name=last_name,contact=contact, dob=dob, blood=blood, district=district, city=city, ward=ward, gender=gender)
        
        data.save()
        print("data saved")
        return redirect('/')
      else:
          return render(request, 'create_donor.html')
        




    


    