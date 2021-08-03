from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
    
from app.models import Allmatchs

def showdata(request):
    results = Allmatchs.objects.all()
    return render(request, 'home.html', {"data":results})
