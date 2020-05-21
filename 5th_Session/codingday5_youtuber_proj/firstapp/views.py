from django.shortcuts import render
from .models import youtuber

# Create your views here.
def home(request):
    youtube = youtuber.objects
    
    return render(request, 'home.html', {'youtube': youtube})