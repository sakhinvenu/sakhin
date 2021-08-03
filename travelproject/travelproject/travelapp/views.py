from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Team


# Create your views here.

def demo123(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'results': obj,'result':obj1})
