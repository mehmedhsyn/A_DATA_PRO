from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from django.utils import timezone
# Create your views here.
    
from app.models import Allmatchs, Nextmatchs, WinLose

def showdata(request):
    results = Allmatchs.objects.all()
    return render(request, 'home.html', {"data":results})

def nextdata(request):
    results = Allmatchs.objects.all()
    weekend_list = []

    for list_of_matches in results.values():
        time_now = timezone.now()
        first_match_date = list_of_matches['data']
        print(first_match_date, time_now-timezone.timedelta(days=3))
        if(first_match_date < time_now-timezone.timedelta(days=3)):
            continue

        for i in results.values():
            match_date = i['data']
            if(match_date < first_match_date+timezone.timedelta(days=4) and match_date >= first_match_date):
                weekend_list.append(i)

        break

    return render(request, 'nextmatches.html', {"data": weekend_list})
    


#def nextdata(request):
 #   results = Nextmatchs.objects.all()
  #  return render(request, 'nextmatches.html', {"data":results})

def winlosedata(request):
    results = WinLose.objects.all()
    return render(request, 'win_loss.html', {"data":results})


