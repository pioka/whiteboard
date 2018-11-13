from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.
def studentHome(request):
    article_list = Article.objects.filter(archived=False).order_by('-id')

    context = {
        'article_list': article_list,
    }
    return render(request, 'board/studentHome.html', context)


@login_required
def teacherHome(request):
    article_list = Article.objects.filter(archived=False).order_by('-id')

    context = {
        'article_list': article_list,
    }
    return render(request, 'board/teacherHome.html', context)

@login_required
def teacherCreateArticle(request):
    return render(request, 'board/teacherCreateArticle.html')
