from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('gallery1',views.gallery1,name="gallery1"),
    path('gallery',views.gallery,name="gallery"),
    path('sample',views.sample,name="sample"),
    path('services',views.services,name="services"),

]