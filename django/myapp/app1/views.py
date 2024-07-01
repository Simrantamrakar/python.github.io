from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("hello from new app1")