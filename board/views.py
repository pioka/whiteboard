from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

from .models import Article, Board
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'board/index.html')


def list_articles(request, board_id):
    try:
        board = Board.objects.get(id=board_id)
    except Board.DoesNotExist:
        raise Http404('Board does not exist')

    articles = Article.objects.filter(board_id=board_id).order_by('-id')

    context = {
        'board': board,
        'articles': articles,
    }

    return render(request, 'board/list_articles.html', context)


@login_required
def create_article(request, board_id):
    try:
        board = Board.objects.get(id=board_id)
    except Board.DoesNotExist:
        raise Http404('Board does not exist')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.is_archived = False
            obj.board = board
            obj.save()
            return HttpResponseRedirect(str(board.id))
    else:
        form = ArticleForm()

    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'board/create_article.html', context)
