#Django
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
import json
#Models
from .models import Quiz

url = "https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean"


@csrf_protect
def quiz_app(request):
    '''quiz api'''
    response = requests.get(url)
    data = response.json()
    quiz = Quiz.objects.all()#queryset from DB
    #control variables
    count = 1
    final_result = 0
    response = ''
    '''If there are something in DB, if not save data in DB to
    don't get random values from url'''
    if quiz:
        return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],#specific info needed
        'count':count,
        'final_result':final_result,
        'response':response})
    else:
        quiz = Quiz.objects.create(data=data)
        return render(request, 'test/quiz.html', {
        'results': quiz.data['results'],
        'count':count,
        'final_result':final_result,})

def question(request):
    '''advance through questions'''
    quiz = Quiz.objects.all()
    #control variable from html
    count = int(request.POST.get('counter'))
    final_result = int(request.POST.get('final_result_data'))
    answer_data = request.POST.get('answer')
    response = str(request.POST.get('response_data'))
    #get answer to campare with answer given from page
    answers = quiz[0].data['results'][count-1]
    if answers['correct_answer'] == answer_data:
        final_result = final_result+1
        response =  response + answers['question']  + ' CORRECT!! '
    else:
        response =  response + answers['question'] + ' INCORRECT!!'
    count = count+1
    #count number of questions when finish go to results page
    if count > 10:
        responses = response.split("!!")
        return render(request,'test/results.html',{'final_result':final_result, 'responses':responses})
    return render(request, 'test/quiz.html', {
        'results': quiz[0].data['results'],
        'count':count,
        'final_result':final_result,
        'response':response})

def home_page(request):
    '''show main page'''
    return render(request, 'test/main.html')