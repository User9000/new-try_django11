from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation

# Create your views here.

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'

    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name,context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()

class MexicanRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='mexican')

class AsianFusionRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')