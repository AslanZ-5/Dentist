from django.forms import ModelForm
from blog.models import Blog


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']
