from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index (request):
    print "CHECKPOINT: Thanks for joining us. You are going to Landing."
    return render(request, 'amazingKidsApp/index.html')

def curriculum(request):
    print "CHECKPOINT: Thanks for joining us. You are going to corriculum."
    return render(request, "amazingKidsApp/curriculum.html")