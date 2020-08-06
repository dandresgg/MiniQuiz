#Django
from django.urls import path
#Views
from . import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('quiz/', views.quiz_app, name='quiz'),
    path('question/',views.question, name='question')
]
