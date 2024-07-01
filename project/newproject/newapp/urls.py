from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add', views.addemployee, name='addemployee'),
    path('delete', views.deletteemployee, name="deletteemployee")
    
]
