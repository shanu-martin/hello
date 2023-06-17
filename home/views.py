from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from test import *
# from datetime import datetime
def Main(request):
    try:
        if request.method == "POST":
            search= request.POST.get("search")
        if search!='':
            return redirect(f'https://www.google.com/search?client=firefox-b-d&q={search}+ice+cream')
    except:
        return render(request,"Main.html")
   
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def order(request):
    return render(request,"order.html")
def contact(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        complaint= request.POST.get("complaint")
        contact=Contact(name=name,email=email,complaint=complaint)
        contact.save()
        messages.success(request, "You have raised a complaint...")
    return render(request,"contact.html")

def buy(request):
    return redirect(f'https://www.amazon.in/ice-cream/s?k=icecreams')