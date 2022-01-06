from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.hiretuber,name="hiretuber")
]