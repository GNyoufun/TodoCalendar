from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
# Create your views here.

def todoAddOn(request):
    if request.method == 'POST':
        form = forms.Todo(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/todo/')
    else:
        form = forms.Todo()
    return render(request, "TodoAddOn.html", {'form': form})