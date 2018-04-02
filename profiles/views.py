from django.crontrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.

User = get_user_model()

class ProfileDetailView(DetailView):
    queryset = User.objects.fiter(is_acitve=True)

