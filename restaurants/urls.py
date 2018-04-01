
from django.conf.urls import url
from django.contrib import admin
from restaurants.views import RestaurantCreateView,RestaurantListView, RestaurantDetailView, RestaurantUpdateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [


    #url(r'^(?P<slug>[\w-]+)/edit/$',RestaurantUpdateView.as_view(), name='update' ),
    url(r'^create/$',RestaurantCreateView.as_view(), name='create' ),#  restaurant_createview
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(),name='detail'),
    url(r'^$', RestaurantListView.as_view(),name='list'),

]
