from django.shortcuts import get_object_or_404, render, redirect
from .models import Time, Author, Article
from django.db.models import Count


def homepage(request):
    authors = Author.objects.all()
    article = Article.objects.annotate(
        num_likes=Count('likes')
    ).order_by('-num_likes')

    
    return render(request, 'main/homepage.html', {'authors': authors, 'articles': article})

# def article_detail(request, article_id):
#     article = get_object_or_404(Article, id=article_id, is_published=True)
#     return render(request, 'main/article_detail.html', {'article': article})
