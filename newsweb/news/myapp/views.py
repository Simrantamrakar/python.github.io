from django.shortcuts import render, HttpResponse,redirect
from . models import NewsCategori, NewsDetails, NewsAbout, Details, Contact, Info
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView, DetailView ,DeleteView, UpdateView
from .forms  import ContactForm, ContactModelForm
import requests


def index(request):
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()
    studentlist = data.get('data')
    news = NewsDetails.objects.all()
    allnews= NewsDetails.objects.all()[:4]
    anc=  news[:1]
    bottom = news[1:4]
    print(studentlist)
    
    return render(request,'myapp/index.html',{ 'all_news': allnews, 'singlenews':anc,'bottom': bottom,'studentlist':studentlist})




def news_details(request, slug):
    # data = request.session['news']
    # print(data)
    # dis = request.session['disc']
    # print(dis)
    related_news = NewsDetails.objects.get(news_slug=slug) # select * from abc where id =1
    return render(request,'myapp/details.html',{'realtednews':related_news})


def about(request):
    allabout= Details.objects.first()
    # data =request.session['news']
    # print(data)
    # print(allabout)
    allxyz= Details.objects.first()
    # dis= request.session['disc']
    # print(dis)
    return render(request,'myapp/about.html',{'about': allabout, 'detail': allxyz} )

def contact(request): 
    if request.method == "POST":
        name= request.POST['username']
        messages= request.POST['message']
        email= request.POST['email']
        subject= request.POST['subject']
        contactinfo = Contact(name= name, message= messages, email= email, subject= subject) 
        contactinfo.save()

        #mail sending 
        subject = "thank you."
        message = "thank you for contacting."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

        # mail for admin user

        subject = "customer querie."
        message = "name: "+name + "email: "+email + "subject: "+subject + "message: "+message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]
        send_mail(subject, message, email_from, recipient_list)
       
    allinfo= Info.objects.first()
    return render(request,'myapp/contact.html',{'info': allinfo})

# #def blog(request):
#     return render(request,'myapp/blog.html')
def form(request):
    contact_form = ContactModelForm()
    #model form
    if request.method  == "POST" :
        formdata = ContactModelForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect("index")
    else:
        return render(request,'myapp/form.html',{'contactform':contact_form})

    # form
    # if request.method  == "POST" :
    #     formdata = ContactForm(request.POST)
    #     if formdata.is_valid():
    #         name = formdata.cleaned_data.get('name')
    #         email = formdata.cleaned_data.get('email')
    #         message = formdata.cleaned_data.get('message')
    #         subject = formdata.cleaned_data.get('subject')
    #         forminfo= Contact(name= name,email = email, subject=subject, message= message)  
    #         forminfo.save()
    #         return redirect("index")
    # else:
    #     return render(request,'myapp/form.html',{'contactform':contact_form})

# class Form(ListView):
#     model= Contact
#     template_name= 'myapp/form/html'
#     fields= 
#     context_object_name='form'


class Bloglistview(ListView):
    queryset= NewsDetails.objects.all()
    template_name= 'myapp/blog.html'
    context_object_name= 'blogs'

class BlogDetail(DetailView):
    model= Details
    template_name= 'myapp/details.html'
    context_object_name= 'realtednews'

class Delete(DeleteView):
    model= Details
    template_name= 'myapp/delete.html'
    success_url='/'

class Update(UpdateView):
    model= Details
    fields= ["image","title","discriptions"]
    template_name= 'myapp/update.html'
    success_url='/'



def details(request):
    return render(request,'myapp/details.html')

def elements(request):
    return render(request,'myapp/elements.html')

def latestnews(request):
    return render(request,'myapp/latest_news.html')

def main(request):
    return render(request,'myapp/main.html')

def singleblog(request):
    return render(request,'myapp/single-blog.html')

def categori(request):
    allcategori =  NewsCategori.objects.all()
    #abc = allcategori[:5]
    # print(allcategori)
    # for item in allcategori:
    #     print(item)
    #     for i in item.newcategori.all():
    #         print(i)
    allnews= NewsDetails.objects.all()
        
    return render(request,'myapp/categori.html',{'categories':allcategori,
                                                 'all_news':allnews
                                                 })




