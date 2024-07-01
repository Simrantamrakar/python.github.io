from django.urls import path
from . import views
from . views import NewsCategoriListView, NewCategoriesCreatView


urlpatterns = [
    path('', NewsCategoriListView.as_view(), name='listview'),
    path('create', NewCategoriesCreatView.as_view(),name= 'createview')
]

