from django.shortcuts import render
def home(request):
    return render(request,'firstapp_templates/home.html' )

def first(request):
    return render(request,'firstapp_templates/first.html')

def second(request):
    return render(request,'firstapp_templates/second.html')

def third(request):
    return render(request,'firstapp_templates/third.html')