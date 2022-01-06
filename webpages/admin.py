from django.contrib import admin
from . models import *
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="80" />',format(object.photo.url))

    list_display = ("id","myphoto","first_name","role","created_time")
    list_display_links = ('id','first_name')

class SliderDisplay(admin.ModelAdmin):

    def sliderphoto(self,object):
        return format_html("<img src='{}' width='250' />",format(object.photo.url))

    list_display = ['headline','sliderphoto','button_text']

class Info_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('heading',)

class about_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Slider,SliderDisplay)
admin.site.register(team,TeamAdmin)
admin.site.register(contact_us)
admin.site.register(info,Info_admin)
admin.site.register(about_detail,about_admin)