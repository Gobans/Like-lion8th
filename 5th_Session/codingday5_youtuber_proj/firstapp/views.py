from django.shortcuts import render
from .models import youtuber
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
def create(request):
    Youtuber = youtuber()
    Youtuber.ch_name = request.POST['name']
    Youtuber.cr_name = request.POST['creator']
    Youtuber.subscr = request.POST['subscribe_num']
    Youtuber.vi_link1 = request.POST['youtube_link_1']
    Youtuber.vi_link2= request.POST['youtube_link_2']
    Youtuber.vi_link3 = request.POST['youtube_link_3']
    Youtuber.summary = request.POST['summary']
    Youtuber.text = request.POST['text']
    Youtuber.on_off = request.POST['text']
    Youtuber.save()
    return redirect('home')

def home(request):
    youtube = youtuber.objects
    return render(request, 'home.html', {'youtube': youtube})

def detail(request,detail_id):
    detail = get_object_or_404(youtuber,pk= detail_id)
    return render(request,'detail.html',{'content':detail})

def new(request):
    return render(request,'new.html')