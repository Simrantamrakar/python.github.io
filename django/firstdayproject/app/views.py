from django.shortcuts import render, HttpResponse


def index(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def birds(request):
    return render(request,'app/birds.html')

def testimonial(request):
    return render(request,'app/testimonial.html')
