from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import Hire
from django.contrib import messages
# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            user_id = request.POST['user_id']
        except MultiValueDictKeyError:
            user_id = False
        tuber_id = request.POST['tuber_id']
        email = request.POST['email']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']

        data = Hire(
            first_name=first_name,
            last_name=last_name,
            tuber_id=tuber_id,
            user_id=user_id,
            email=email,
            tuber_name=tuber_name,
            city=city,
            state=state,
            phone=phone,
            message=message
        )
        data.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('youtubers')


