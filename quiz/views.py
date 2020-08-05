from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
import json

from .models import Quiz
# Create your views here.
url = "https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean"

@csrf_protect
def quiz_app(request):
    '''quiz api'''
    response = requests.get(url)
    data = response.json()
    quiz = Quiz.objects.all()
    if quiz:
        print(quiz[0].data['results'])
        return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
    })
    else:
        quiz = Quiz.objects.create(data=data)
        return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
        })