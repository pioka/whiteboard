from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article, Board
from .forms import ArticleForm


#### Views ####
# index
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}

    return render(request, 'board/index.html', context)


# お知らせをリスト表示
def list_articles(request, username, board_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, owner=owner, id=board_id)
    articles = Article.objects.filter(board=board, is_archived=False).order_by('-updated_at')

    context = {
        'board': board,
        'articles': articles, 
    }

    return render(request, 'board/list_articles.html', context)


def all_articles(request, username, board_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, owner=owner, id=board_id)
    article_list = Article.objects.filter(board=board)
    paginator = Paginator(article_list, 10, orphans=5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'board': board,
        'articles': articles, 
    }

    return render(request, 'board/all_articles.html', context)


@login_required
def create_article(request, username, board_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, owner=owner, id=board_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.is_archived = False
            new_article.board = board
            new_article.save()
            return HttpResponseRedirect(
                reverse('list_articles', args=[board.owner.username, board.id])
            )
    else:
        form = ArticleForm()

    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'board/create_article.html', context)


@login_required
def edit_article(request, username, board_id, article_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, id=board_id, owner=owner)
    article = get_object_or_404(Article, board=board, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.subject = form.cleaned_data['subject']
            article.body = form.cleaned_data['body']
            article.save()
            return HttpResponseRedirect(
                reverse('list_articles', args=[board.owner.username, board.id])
            )
    else:
        form = ArticleForm(initial={
            'subject': article.subject,
            'body': article.body,
        })

    context = {
        'article': article,
        'board': board,
        'form': form,
    }
    return render(request, 'board/edit_article.html', context)


@login_required
def account_settings(request):
    pass

@login_required
def archive_article(request, username, board_id, article_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, id=board_id, owner=owner)
    article = get_object_or_404(Article, board=board, id=article_id)

    if request.method == 'POST' and request.user == owner:
        article.is_archived = True
        article.save()
    
    return HttpResponseRedirect(
        reverse('list_articles', args=[board.owner.username, board.id])
    )


@login_required
def restore_article(request, username, board_id, article_id):
    owner = get_object_or_404(User, username=username)
    board = get_object_or_404(Board, id=board_id, owner=owner)
    article = get_object_or_404(Article, board=board, id=article_id)

    if request.method == 'POST' and request.user == owner:
        article.is_archived = False
        article.save()
    
    return HttpResponseRedirect(
        reverse('list_articles', args=[board.owner.username, board.id])
    )
