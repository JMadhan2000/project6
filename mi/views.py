from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Rohith(request):
    return render(request,'rohith.html')


def abd(request):
    return HttpResponse('<h1>ABD is the Mr 360</h1>')