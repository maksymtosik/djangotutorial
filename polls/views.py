from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    latestQuestions = Question.objects.order_by('-publicationDate')[:5]
    context = {'latestQuestions': latestQuestions} # dictionary -> jinja object
    return render(request, 'polls/index.html', context)

def construction(request):
    return HttpResponse("Remont kosciola wejscie od zachrystii")

def details(request, questionID):
    question = get_object_or_404(Question, pk=questionID) # get or 404 is equvalent of commented method
    return render(request, 'polls/details.html', {'question':question})

def choices(request, choiceID):
    choice = get_object_or_404(Question, pk=choiceID) # czemu question a nie choice?
    return render(request, 'polls/choices.html', {'choice': choice})

def results(request, questionID):
    response = 'Results of question no.  %s'
    return HttpResponse(response % questionID) # also legal syntax

def votes(request, questionID):
    return HttpResponse('Voting for question no.  %s' % questionID)