from main.models import Time, Author, Article, Comment
from django.forms import ModelForm, TextInput, Textarea, FileInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'main_content', 'image']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'main_content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of article'}),
            'image': FileInput(attrs={'class': 'form-control'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content_of_comment']
        
        widgets = {
            'content_of_comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'write something...', 'rows': 2, 'cols': 50})
        }