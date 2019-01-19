from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import ArticleForm
from django.urls import reverse


class ArticleListView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'


class IndexView(ArticleListView):

    def get_queryset(self):
        articles = Article.objects.all()
        return articles


def detail_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article=article)
    if comments.count() == 0:
        comments = None
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'blog/detail_article.html', context)


class CreateView(generic.FormView):
    template_name = 'blog/create_blog.html'


def create_view(request):
    form = ArticleForm
    context = {
        'form': form,
    }
    return render(request, 'blog/create_blog.html', context)


def create_action(request):
    title = request.POST['title']
    context = request.POST['context']
    Article.objects.create(title=title, context=context)
    return HttpResponseRedirect(reverse('blog:index'))


def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment_text = request.POST['comment']
    Comment.objects.create(article=article, comment=comment_text, comment_date=now())
    return HttpResponseRedirect(reverse('blog:detail', args=(article_id,)))
