from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'app/index.html')
    
    

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def gallery1(request):
    return render(request,'app/gallery1.html')

def gallery(request):
    return render(request,'app/gallery.html')

def sample(request):
    return render(request,'app/sample-inner-page.html')

def services(request):
    return render(request,'app/services.html')


