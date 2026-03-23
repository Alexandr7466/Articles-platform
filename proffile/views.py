from django.shortcuts import get_object_or_404, render, redirect
from main.models import Time, Author, Article
# from .forms import AuthorForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm


def profile_page(request):
    articles = None
    if request.user.is_authenticated:
        try:
            author = request.user.author
            articles = author.articles.all()
        except Author.DoesNotExist:
            articles = []
    return render(request, 'proffile/profile_page.html', {'articles': articles})

def profile_page_of_someone(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    author, created = Author.objects.get_or_create(user=user)
    articles = author.articles.all()
    
    return render(request, 'proffile/profile_page_of_someone.html', {
        'author': author,
        'articles': articles
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.get_or_create(user=user)
            login(request, user)

            return redirect('proffile:profile_page')
    else:
        form = RegisterForm()
    
    return render(request, 'proffile/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('homepage')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('proffile:profile_page')
    
    else: 
        form = LoginForm()

    return render(request, 'proffile/log_in.html', {'form': form})

def menu(request):
    return render(request, 'proffile/menu.html')