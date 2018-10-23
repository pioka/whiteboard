from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    article_list = Article.objects.filter(archived=False).order_by('-id')

    context = {
        'page': 'Home',
        'article_list': article_list
    }
    return render(request, 'board/index.html', context)


def archivedArticles(request):
    article_list = Article.objects.filter(archived=True).order_by('-id')

    context = {
        'page': 'Archived',
        'article_list': article_list
    }
    return render(request, 'board/index.html', context)
