from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path ('', views.homepage, name='homepage'),
    # path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]