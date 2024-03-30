from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "isnewyear/index.html", {"yes":now.day == 1 and now.month == 1})