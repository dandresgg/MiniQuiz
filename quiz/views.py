from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
# Create your views here.
url = "https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean"

@csrf_protect
def quiz_app(request):
    '''quiz api'''
    response = requests.get(url)
    data = response.json()
    return render(request, 'test/quiz.html', {
        'results': data['results'],
    })