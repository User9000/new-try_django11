from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required()
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            #form.save()
            return HttpResponseRedirect('/restaurants/')
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

        
    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}

    return render(request, template_name, context)


# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'

    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name,context)


def restaurant_detailtview(request, slug):
    template_name = 'restaurants/restaurants_detail.html'

    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object":obj,
    }
    return render(request, template_name,context)


### Filter by Restaurant Category
class RestaurantListView(ListView):
    
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug)
                 | Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset
    
    
    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(RestaurantListView,self).get_context_data(*args, **kwargs)
        print(context)    
        return context


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_detail.html'


"""   def get_object(self, *args, **kwargs ):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id)
        return obj
"""

class RestaurantCrateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    sucess_url = '/restaurants/'
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCrateView,self).get_context_data(*args, **kwargs)
        context['title']='Add Restaurant'
        return context

