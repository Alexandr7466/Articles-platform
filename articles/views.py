from django.shortcuts import get_object_or_404, render, redirect
from main.models import Time, Author, Article
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            author, created = Author.objects.get_or_create(user=request.user)
            article.author = author
            time = Time.objects.create()
            article.is_published = True
            article.time = time
            
            article.save()

            return redirect('homepage')
    else: 
        form = ArticleForm()

    data = {
        'form': form ,
    }

    return render(request, 'articles/create.html', data)

def article_detail(request, id):
    article = get_object_or_404(Article, id=id, is_published=True)
    comments = article.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()

            return redirect('articles:article_detail', id=article.id)

    else:
        form = CommentForm()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })

def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True

    return JsonResponse({
        "liked": liked,
        "count": article.likes.count(),
    })

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    
    if request.user.is_authenticated:
        # if request.user not in article.views.all():
        if not article.views.filter(id=request.user.id).exists():
            article.views.add(request.user)
            viewed = True

    return JsonResponse({"count_views": article.views.count(),})

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if article.author.user != request.user:
        return redirect('articles:article_detail', article_id=article.id)
    
    if request.method == 'POST':
        article.delete()  
        return redirect('homepage')  
    
    return render(request, 'articles/confirm_delete.html', {'article': article})

