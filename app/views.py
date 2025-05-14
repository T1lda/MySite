from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FeedbackForm  # Импорт из forms.py
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import CommentForm
from datetime import datetime
from .models import Blog, Comment
from django.contrib.auth.decorators import user_passes_test
from .forms import BlogForm

def home(request):
    """Главная страница."""
    return render(
        request,
        'app/index.html',
        {'title': 'Главная', 'year': datetime.now().year}
    )

def contact(request):
    """Страница контактов."""
    return render(
        request,
        'app/contact.html',
        {'title': 'Контакты', 'message': 'Свяжитесь с нами', 'year': datetime.now().year}
    )

def about(request):
    """О проекте."""
    return render(
        request,
        'app/about.html',
        {'title': 'О нас', 'message': 'Описание проекта', 'year': datetime.now().year}
    )

def feedback(request):
    """Обратная связь."""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = {key: form.cleaned_data[key] for key in form.cleaned_data}
            return render(request, 'app/feedback.html', {'data': data})
        return render(request, 'app/feedback.html', {'form': form})
    return render(request, 'app/feedback.html', {'form': FeedbackForm()})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/registration.html', {'form': form})

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-date')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.date = datetime.now()
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'app/blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def blog_list(request):
    posts = Blog.objects.all().order_by('-posted')  # Сортировка по дате (новые сверху)
    return render(request, 'app/blog_list.html', {'posts': posts, 'title': 'Блог'})



class BootstrapAuthenticationForm(AuthenticationForm):
    """Кастомная форма входа."""
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

@user_passes_test(lambda u: u.is_superuser)
def new_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Автоматически назначаем автора
            post.save()
            return redirect('blog_detail', pk=post.id)
    else:
        form = BlogForm()
    return render(request, 'app/new_post.html', {'form': form})

def videopost(request):
    return render(request, 'app/videopost.html')
def current_year():
    return datetime.now().year
def links(request):
    return render(
        request,
        'app/links.html',
        {'title': 'Полезные ресурсы', 'year': datetime.now().year}
    )