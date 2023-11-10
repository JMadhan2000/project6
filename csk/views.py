from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def Bhumrah(request):
    return HttpResponse('<h1>Bhumrah is the best bowler in the Indian cricket team</h1>')