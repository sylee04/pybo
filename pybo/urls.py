from django.urls import path

#from . import views
from .views import base_views, question_views, answer_views, vote_views


app_name = 'pybo'

urlpatterns = [
    # path('', views.index),
    # path('<int:question_id>/', views.detail),
    #path('', views.index, name='index'),
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer')


    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # path('question/create/', views.question_create, name='question_create'),
    # path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # path('vote/question/<int:question_id>/', views.vote_question, name='vote_question'),

]