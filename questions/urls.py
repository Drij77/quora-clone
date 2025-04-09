from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('question/new/', views.question_create, name='question-create'),
    path('question/<int:pk>/', views.question_detail, name='question-detail'),
    path('answer/<int:pk>/like/', views.like_answer, name='like-answer'),
] 