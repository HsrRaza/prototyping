from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("Hello , world ,Home Page chai aur code")
    return render(request ,'index.html')
    

def about(request):
    return HttpResponse("Hello , world , About Page chai aur code")

def contact(request):
    return HttpResponse("Hello , world ,Contact page chai aur code")