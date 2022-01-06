from django.contrib import admin
from .models import Hire
# Register your models here.

class display(admin.ModelAdmin):
    list_display = ['first_name','tuber_name','email']


admin.site.register(Hire,display)