from django.shortcuts import render
from .models import Orders,Members,Sheets,Goods
# Create your views here.

def home(request):
    Sheets_rows = Sheets.objects.all()
    return render(request, 'index.html', {"Sheets_rows": Sheets_rows})