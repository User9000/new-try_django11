
from django.conf.urls import url


from .views import (

    ItemCreateView,
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
)
urlpatterns = [
  
    url(r'^create/$',ItemCreateView.as_view(), name='create' ),#  restaurant_createview
    url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(),name='update'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(),name='detail'),
    url(r'^$', ItemListView.as_view(),name='list'),
  

]
