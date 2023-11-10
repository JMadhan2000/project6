from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Virat(request):
    return render(request,'virat.html')

def maxwell(request):
    return HttpResponse('<h1>Maxwell is best batsman</h1>')
