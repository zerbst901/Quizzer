from django.urls import path
from . import views

urlpatterns = [

    path('start', views.start,name='start'),
    path('cook', views.create, name='create_quiz'),
    path('test/<int:quiz_id>', views.conduct_quiz, name='test'),

    ]