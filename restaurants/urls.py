
from django.conf.urls import url
from django.contrib import admin
from restaurants.views import restaurant_listview, RestaurantCrateView,RestaurantListView, RestaurantDetailView, restaurant_createview
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [


    url(r'^$', RestaurantListView.as_view(),name='list'),
    url(r'^create/$',RestaurantCrateView.as_view(), name='create' ),#  restaurant_createview
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='detail'),

]
