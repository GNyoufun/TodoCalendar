from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from . import forms

from datetime import date

import calendar 


# Create your views here.

def home(request, year=date.today().year, month = date.today().month):
    if month > 12 or month < 1:
        messages.warning(request, "The month entered are invalid, please enter valid month.")
        month = date.today().month

    first, numDay = calendar.monthrange(year, month)
    if (year == date.today().year and month == date.today().month):
        today =  date.today().day
    else:
        today = 0
    
    month = list(calendar.month_name)[month]

    return render(request, 'home.html', {
                    "year": year, 
                    "month": month, 
                    "first": first, 
                    "numDay": numDay,
                    "today": today,
                    })

def todoAddOn(request):
    if request.method == 'POST':
        form = forms.Todo(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/todo/')
    else:
        form = forms.Todo()
    return render(request, "TodoAddOn.html", {'form': form})