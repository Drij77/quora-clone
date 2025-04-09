from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer
from .forms import UserRegisterForm, QuestionForm, AnswerForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'questions/register.html', {'form': form})

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/home.html', {'questions': questions})

@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Your question has been posted!')
            return redirect('question-detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'questions/question_form.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('-created_at')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, 'Your answer has been posted!')
            return redirect('question-detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'questions/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return HttpResponseRedirect(reverse('question-detail', args=[answer.question.pk])) 