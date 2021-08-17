from crawler.crawler import all_matches
from django.shortcuts import render, HttpResponse
from django.utils.translation import templatize
from django.views.generic import TemplateView
from datetime import datetime
from django.utils import timezone
from django.views.generic import ListView
# Create your views here.
from .models import Allmatchs, WinLose, Nextmatchs
    
from app import models

class AllView(ListView):
    model = Allmatchs
    template_name = 'home.html'
    

class NextView(ListView):
    model = Allmatchs
    template_name = 'nextmatches.html'
    weekend_list = []

    for list_of_matches in model.objects.all():
        print(list_of_matches.__dict__)
        first_match_date = list_of_matches.datа
        print(first_match_date, time_now-timezone.timedelta(days=3))
        if(first_match_date < time_now-timezone.timedelta(days=3)):
            continue

        for i in model.objects.all():
            match_date = i
            if(match_date < first_match_date+timezone.timedelta(days=4) and match_date >= first_match_date):
                weekend_list.append(i)

        break


    
#def nextdata(request):
 #   results = Allmatchs.objects.all()
  #  weekend_list = []

   # for list_of_matches in results.values():
    #    time_now = timezone.now()
     #   first_match_date = list_of_matches['data']
      #  print(first_match_date, time_now-timezone.timedelta(days=3))
       # if(first_match_date < time_now-timezone.timedelta(days=3)):
        #    continue

        #for i in results.values():
         #   match_date = i['data']
          #  if(match_date < first_match_date+timezone.timedelta(days=4) and match_date >= first_match_date):
           #     weekend_list.append(i)

        #break

    #return render(request, 'nextmatches.html', {"data": weekend_list})

class RankingView(ListView):
    model = WinLose
    template_name = 'win_loss.html'


