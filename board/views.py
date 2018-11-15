from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.
def home(request):
    article_list = Article.objects.filter(archived=False).order_by('-id')

    context = {
        'article_list': article_list,
    }

    return render(request, 'board/home.html', context)

@login_required
def createArticle(request):
    return render(request, 'board/createArticle.html')
