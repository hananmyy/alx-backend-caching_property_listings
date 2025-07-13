from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import Property
from properties.utils import get_redis_cache_metrics
from django.http import JsonResponse
from .utils import get_all_properties


"""@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})"""

def property_list(request):
    properties = get_all_properties()

    return JsonResponse({'data': properties})



print(get_redis_cache_metrics())