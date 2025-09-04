from django.shortcuts import render
from datetime import date

def home(request):
    return render(request, "home.html", {"today": date.today()})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
