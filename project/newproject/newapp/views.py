from django.shortcuts import render,HttpResponse,redirect
from . models import Employee

def index(request):
    employees= Employee.objects.all()
    # print(employees)
    # for a in employees:
    #     print(a)
    return render(request,'newapp/home.html',{'employee':employees})

# Create your views here.



def addemployee(request):
    if request.method =="POST":
        fullname = request.POST['fullname']
        print(fullname)
        email = request.POST['email']
        address = request.POST['address']
        phone= request.POST['phone']
        print(phone)
        empl_obj = Employee(name=fullname, email =email, address = address, phone= phone)
        empl_obj.save()
        return redirect('index')
















def deletteemployee(request):
    if request.method == "POST":
        empid = request.POST['emplid']
        print(empid)
        emp_obj = Employee.objects.get(id= empid)  # slect * from employyee where id =1
        emp_obj.delete()
        return redirect('index')
    return redirect('index')

    