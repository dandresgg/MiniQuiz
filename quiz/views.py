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
    count = 1
    final_result = 0
    response = ''
    if quiz:
        return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
        'count':count,
        'final_result':final_result,
        'response':response})
    else:
        quiz = Quiz.objects.create(data=data)
        return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
        'count':count,
        'final_result':final_result,})

def question(request):
    '''advance questions'''
    quiz = Quiz.objects.all()
    count = int(request.POST.get('counter'))
    final_result = int(request.POST.get('final_result_data'))
    answer_data = request.POST.get('answer')
    answers = quiz[0].data['results'][count-1]
    response = str(request.POST.get('response_data'))
    if answers['correct_answer'] == answer_data:
        final_result = final_result+1
        response =  response + answers['question']  + ' CORRECT!! '
    else:
        response =  response + answers['question'] + ' INCORRECT!!'
    count = count+1
    if count > 10:
        responses = response.split("!!")
        print(responses)
        return render(request,'test/results.html',{'final_result':final_result, 'responses':responses})
    print(final_result)
    return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
        'count':count,
        'final_result':final_result,
        'response':response})

