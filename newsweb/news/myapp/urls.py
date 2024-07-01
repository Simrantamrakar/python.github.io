from django.urls import path
from . import views
from . views import Bloglistview, BlogDetail, Delete, Update

urlpatterns = [
    path('', views.index,name='index'),
    path('newsdetails/<slug:slug>',views.news_details,name="newsdetails"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('form',views.form,name= "form"),
    path('blog', Bloglistview.as_view(),name= 'blog' ),
    path('details/<int:pk>',BlogDetail.as_view(),name= 'blogdetail'),
    path('delete/<int:pk>',Delete.as_view(),name="Delete"),
    path('blogupdate/<int:pk>/update',Update.as_view(),name='Update'),
    #path('blog',views.blog,name="blog"),
    path('categori',views.categori,name="categori"),
    path('details',views.details,name="details"),
    path('elements',views.elements,name="elements"),
    path('latestnews',views.latestnews,name="latestnews"),
    path('main',views.main,name="main"),
    path('singleblog',views.singleblog,name="singleblog"),
]   