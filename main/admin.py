from django.contrib import admin
from .models import Time, Author, Article, Comment

admin.site.register(Time)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
