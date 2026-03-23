from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User

class Time (models.Model):
    time_of_publication = models.DateTimeField(auto_now_add=True)
    latest_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('time_of_publication',)
        verbose_name = 'Time'
        verbose_name_plural = 'Times'
    
    def __str__(self):
        return str(self.time_of_publication)

class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    
    class Meta:
        ordering = ('user__username',)
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.user.username

class Article(models.Model): 
    title = models.CharField(max_length=100)
    main_content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE) 
    is_published = models.BooleanField(default=False)
    # number_of_views = models.IntegerField(default=0)
    views = models.ManyToManyField(User, related_name='viewed_articles')
    # number_of_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content_of_comment = models.CharField(max_length=100)

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content_of_comment[:30]

