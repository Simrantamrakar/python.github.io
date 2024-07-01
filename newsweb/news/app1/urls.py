from django.urls import path
from . import views


urlpatterns = [
    path('', views.createsession, name='createsession'),
    path('get-session', views.getsession, name='getsession'),
    path('delete-session', views.deletesession, name='deletesession'),
    path('createcookie', views.createcookies, name="createcookie"),
    path('getcookie', views.getcookies, name='getcookie'),
    path('updatecookie', views.updatecookie, name='updatecookie'),
]

