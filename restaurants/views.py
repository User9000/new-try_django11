from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

#Home View
def home(request):
    num = random.randint(0,100000)
    some_list = [num, random.randint(0,100000), random.randint(0,100000)]

    context_ = {
            'html_var':'context variable', 
            "bool_item":False,
            "num":num,
            "some_list": some_list,

    }
    return render(request, "base.html",context_)