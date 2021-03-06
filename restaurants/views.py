from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


### Filter by Restaurant Category
class RestaurantListView(LoginRequiredMixin,ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin,DetailView):
    template_name = 'restaurants/restaurants_detail.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    sucess_url = '/restaurants/'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView,self).get_context_data(*args, **kwargs)
        context['title']='Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'
    #sucess_url = '/restaurants/'
    
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantUpdateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView,self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title']=f'Update Restaurant: {name}'
        return context

