from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def youtubers(request):
    tubers = Ytuber.objects.order_by('-created_date')
    city_search = Ytuber.objects.values_list("city", flat=True).distinct()
    camera_type_search = Ytuber.objects.values_list("camera_type", flat=True).distinct()
    crew_search = Ytuber.objects.values_list("crew", flat=True).distinct()
    data = {
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'crew_search': crew_search,
        'tubers':tubers
    }
    return render(request,'youtubers/youtubers.html',data)

def youtuber_details(request,id):
    tuber = get_object_or_404(Ytuber,pk = id)
    data = {
        'tuber':tuber
    }
    return render(request,'youtubers/youtubers_details.html',data)

def search(request):
    tuber = Ytuber.objects.order_by('-created_date')
    city_search = Ytuber.objects.values_list("city",flat=True).distinct()
    camera_type_search = Ytuber.objects.values_list("camera_type",flat=True).distinct()
    crew_search = Ytuber.objects.values_list("crew",flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tuber = tuber.filter(name__icontains = keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tuber = tuber.filter(city__iexact= city)
    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tuber = tuber.filter(camera_type__iexact=camera)
    if 'crew' in request.GET:
        crew= request.GET['crew']
        if crew:
            tuber = tuber.filter(crew__iexact=crew)

    data = {
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'crew_search': crew_search,
        'tubers' : tuber,
    }
    return render(request,'youtubers/search.html',data)