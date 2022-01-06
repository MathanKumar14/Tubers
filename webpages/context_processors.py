from .models import *

def site_info(request):
    details = info.objects.get()
    data =  {
        'details':details
    }
    return data