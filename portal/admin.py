from django.contrib import admin
from .models import Datasets

admin.site.register(Datasets)
admin.site.site_header = 'Administrator Log in'
admin.site.site_title = 'Admin log in'

# Register your models here.
