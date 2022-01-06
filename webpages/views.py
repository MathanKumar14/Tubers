from django.shortcuts import render,redirect
from .models import *
from youtubers.models import *
from django.contrib import messages
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    team_members = team.objects.all()
    featured_youtubers = Ytuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Ytuber.objects.order_by('-created_date')
    data = {
        'sliders':sliders,
        'team':team_members,
        'featured_youtubers':featured_youtubers,
        'youtubers':youtubers,
    }
    return render(request,'webpages/home.html',data)


def about(request):
    team_members = team.objects.all()
    about_1 = about_detail.objects.get(pk=1)
    about_2 = about_detail.objects.get(pk=2)
    data = {
        'team': team_members,
        'about_1':about_1,
        'about_2':about_2,
    }
    return render(request,'webpages/about.html',data)


def contact(request):
    return render(request,'webpages/contact.html')

def contact_form(request):
    global full_name, phone, email, company_name, subject, message
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

    data = contact_us(
        full_name=full_name,
        phone=phone,
        email=email,
        company_name=company_name,
        subject=subject,
        message=message
    )
    data.save()
    messages.success(request, 'Thanks for reaching out!')
    return redirect('home')

def service(request):
    return render(request,'webpages/service.html')

