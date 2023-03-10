from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
       return render(request,"index.html")


def contact(request):

    if request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,address=address,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'We recieved your message successfully.')
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def product(request):
    return render(request,'product.html')


