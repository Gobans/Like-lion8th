from django.shortcuts import render
from django.utils.safestring import SafeString
from .static.PY.fetch import fetch

# Create your views here.
def index(request):
    return(render(request,'index.html'))

def detail(request,id):
    base = "https://api.themoviedb.org/3/"
    movieid = str(id)
    apiKey = "?api_key=b4104d048776cbde94b18eac3035f9e3"
    URL = base +"movie/"+movieid+apiKey
    data = fetch(URL)


    return(render(request,'detail.html',{'data':data}))