from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Article, Board
from .forms import ArticleForm


#### Helpers ####
def _pick_board(username, board_id):
    try:
        owner = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404('User does not exist')

    try:
        board = Board.objects.get(id=board_id, owner=owner)
    except Board.DoesNotExist:
        raise Http404('Board does not exist')

    return board


#### Views ####
# index
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}

    return render(request, 'board/index.html', context)


# お知らせをリスト表示
def list_articles(request, username, board_id):
    board = _pick_board(username=username, board_id=board_id)

    articles = Article.objects.filter(board_id=board_id).order_by('-id')

    context = {
        'board': board,
        'articles': articles, 
    }

    return render(request, 'board/list_articles.html', context)


@login_required
def create_article(request, username, board_id):
    board = _pick_board(username=username, board_id=board_id)

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
