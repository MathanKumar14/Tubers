from django.contrib import admin
from .models import Ytuber
from django.utils.html import format_html
# Register your models here.

class Ytubers(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="80" />', format(object.photo.url))

    list_display = ('id','name','myphoto','price','is_featured')
    search_fields = ('name','camera_type')
    list_display_links = ('id','name')
    list_filter = ('camera_type',)
    list_editable = ('is_featured',)


admin.site.register(Ytuber,Ytubers)