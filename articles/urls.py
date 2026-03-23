from . import views
from django.urls import include, path

app_name = 'articles'

urlpatterns = [
    path ('', views.create, name='create'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('like/<int:article_id>/', views.like_article, name='like_article'),
    path('view/<int:article_id>/', views.view_article, name='view_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article')
]