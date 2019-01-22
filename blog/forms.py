from django.forms import ModelForm
from .models import Article, User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'context')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
