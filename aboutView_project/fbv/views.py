from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
from django.urls import reverse

# Create your views here.
def index(request):
    # pub_list = Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    return render(request, 'fbv/index.html', {"latest_question_list": latest_question_list})

def vote(request,question_id):
    question =get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (keyError, Choice.DoesNotExit):
        return render(reqeust, 'fbv/detail.html',
        {'question':question, 'error_msg': "you didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('fbv:results', args = (question.id,)))

def detail(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question':question
    }
    return render(request, 'fbv/detail.html', context)

def results(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'fbv/results.html', {"question": question})
    
# def vote(request,question_id):
#     pub_list = Question.objects.all()
#     least5_pub = 
#     return render(request, 'results.html', {"": pub_list})
