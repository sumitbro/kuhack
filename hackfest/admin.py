from django.contrib import admin
from .models import Donor, BloodBank

# Register your models here.
admin.site.register(Donor)
admin.site.register(BloodBank)
