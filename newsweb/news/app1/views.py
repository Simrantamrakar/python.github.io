from django.shortcuts import render, HttpResponse

# Create your views here.

def createsession(request):
    request.session['name']= "RAm thapa"
    request.session.set_expiry(20)
    request.session['address'] ="ktm"
    return HttpResponse("session created successfully !")


def getsession(request):
    try:
        name = request.session['name']
        print(name)
        address = request.session['address']
        print(address)
        return HttpResponse(name)
    except Exception as e:
        print(e)
        return HttpResponse(e)

def deletesession(request):
    del request.session['name']
    return HttpResponse("session delete..")



def createcookies(request):
    username = request.session['name']
    response = HttpResponse("cookie created..")
    response.set_cookie("mycookie", username, 30)
    return response

def getcookies(request):
    name = request.COOKIES['mycookie']
    print(name)
    return HttpResponse("cookie value get succc.....")

def updatecookie(request):
    username = "Hello Nepal"
    response = HttpResponse("cookie update..")
    response.set_cookie("mycookie", username, 30)
    return response