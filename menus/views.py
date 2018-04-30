from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView


from .forms import ItemForm
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):
    def get(self,request, *args, **kwars):
        if not request.user.is_authenticated():
           return render(request, "home.html", {})
        
        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs  = Item.objects.filter(user__id__in=is_following_user_ids, public=True)
        return render(request, "menus/home-feed.html", {'object_list': qs})
    

class ItemListView(LoginRequiredMixin,ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin,DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin,CreateView):
    template_name = 'menus/detail-update.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView,self).form_valid(form)

     #Override get_context_data function#
    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView,self).get_context_data(*args, **kwargs)
        context['title']='Add Menu Item'
        return context
    #Override get_form_kwargs function#
    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        #kwargs['instance'] = Item.objects.filter(user = self.request.user).first()
        return kwargs



class ItemUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'menus/detail-update.html'
    form_class = ItemForm


    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



     #Override get_context_data function#
    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView,self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title']=f'Update Item: {name}'
        return context
    #Override get_form_kwargs function#
    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        #kwargs['instance'] = Item.objects.filter(user = self.request.user).first()
        return kwargs



