#Django
from django.urls import path
#Views
from . import views

urlpatterns = [
    path('',views.quiz_app, name='quiz'),
]