from django.shortcuts import render
from django.http import HttpResponse

def cal (request):
    return render(request,'calculator.html')