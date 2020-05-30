from django.shortcuts import render,get_object_or_404,redirect
from .models import test
from .forms import createForm

# Create your views here.

def create(request):
    Test = test()
    Test.name = request.POST['name']
    Test.summary = request.POST['summary']
    Test.photo = request.FILES['photo']
    Test.save()
    return redirect('home') 

def home(request):
    Test = test.objects
    return render(request, 'home.html',{'test' : Test})

def detail(request,detail_id):
    detail = get_object_or_404(test,pk= detail_id)
    return render(request,'detail.html',{'content':detail})

def new(request):
    form = createForm()
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = createForm()
        return render(request,'new.html', {'form':form})
    else:
        pass