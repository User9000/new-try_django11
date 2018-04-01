from django.shortcuts import render
from django.views.generic import ListView, DetailView, CrateView, UpdateView


from .forms import ItemForm
from .models import Item
# Create your views here.


class ItemListView(ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class DetailListView(ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class CreateListView(ListView):
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



class UpdateListView(ListView):
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)




