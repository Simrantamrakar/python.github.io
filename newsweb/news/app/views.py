from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, CreateView
from myapp.models import NewsCategori


# Create your views here.
# function Based view
def index(request):
    return HttpResponse("hello")


#class Basesd views
class NewsCategoriListView(ListView):
    model = NewsCategori
    template_name = 'app/index.html'
    context_object_name ='new_categories'


class NewCategoriesCreatView(CreateView):
    model = NewsCategori 
    fields = ['categori_name']
    template_name= 'app/newscategori_form.html'
    success_url= "/"
