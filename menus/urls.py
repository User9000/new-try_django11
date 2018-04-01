
from django.conf.urls import url


from .views import (

    ItemCreateView,
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
)
urlpatterns = [


    url(r'^$', RestaurantListView.as_view(),name='list'),
    url(r'^create/$',RestaurantCrateView.as_view(), name='create' ),#  restaurant_createview
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='detail'),

]
