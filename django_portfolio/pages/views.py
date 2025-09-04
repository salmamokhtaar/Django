from django.shortcuts import render
from datetime import date

def home(request):
    return render(request, "home.html", {"today": date.today()})
