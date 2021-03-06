from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update', views.new_requests, name='update-money'),
    path('get_price', views.get_price, name='get_price'),
]
