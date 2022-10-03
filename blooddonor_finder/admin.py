from django.contrib import admin
from .models import BloodGroup,Donor,RequestBlood
# Register your models here.

admin.site.register(BloodGroup)
admin.site.register(RequestBlood)
admin.site.register(Donor)