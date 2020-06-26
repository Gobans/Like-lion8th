from django.shortcuts import render, get_object_or_404 ,redirect
from .models import picture
from django.urls import reverse
from .forms import createForm
import os
# Create your views here.

def home(request):
    picture_obj = picture.objects
    return render(request, 'home.html', {"picture_key":picture_obj})

def update(request,update_id):
    update_obj = get_object_or_404(picture,pk=update_id)
    form = createForm()
    if request.method == "POST":
        update_obj.name = request.POST['name']
        update_obj.explain = request.POST['explain']
        update_obj.photo = request.FILES['photo']
        update_obj.save()
        return redirect(reverse('home'))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj,"form":form})

def create(request):
    form = createForm()
    if request.method == "POST":
        picture_val = picture()
        picture_val.name = request.POST['name']
        picture_val.explain = request.POST['explain']
        picture_val.photo = request.FILES['photo']
        picture_val.save()
        return redirect(reverse('home'))
    else:
        pass
    return render(request, 'create.html',{'form':form})

def delete(request, delete_id):
    delete_obj = get_object_or_404(picture, pk= delete_id)
    delete_obj.delete()
    return redirect('home')