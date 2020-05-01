from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

from .models import Questions,Choice

# Create your views here.

from .models import Questions,Choice

#get questions and display them

def index(request):
    latest_question_list=Questions.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list}

    return render(request,'polls/index.html',context)


#show specific question and choices

def detail(request,question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})

# get question and display results
def results(request,question_id):
    question = get_object_or_404(Questions,pk=question_id)
    return render (request,'polls/results.html',{'question': question})

def vote(request,question_id):
    question = get_object_or_404(Questions,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message':"you didnt select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        
