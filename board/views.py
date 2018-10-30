from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.
def studentHome(request):
    article_list = Article.objects.filter(archived=False).order_by('-id')

    context = {
        'page': 'Home',
        'article_list': article_list
    }
    return render(request, 'board/home.html', context)


def studentArchived(request):
    article_list = Article.objects.filter(archived=True).order_by('-id')

    context = {
        'page': 'Archived',
        'article_list': article_list
    }
    return render(request, 'board/home.html', context)

@login_required
def teacherHome(request):
    return render(request, 'board/home.html')
