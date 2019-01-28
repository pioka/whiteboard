from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list_boards', views.list_boards, name='list_boards'),
    path('edit_board/<int:board_id>', views.edit_board, name='edit_board'),
    path('create_board', views.create_board, name='create_board'),
    path('<str:username>/board/<int:board_id>/', views.list_articles, name='list_articles'),
    path('<str:username>/board/<int:board_id>/all', views.all_articles, name='all_articles'),
    path('<str:username>/board/<int:board_id>/create_article', views.create_article, name='create_article'),
    path('<str:username>/board/<int:board_id>/article/<int:article_id>/edit', views.edit_article, name='edit_article'),
    path('<str:username>/board/<int:board_id>/article/<int:article_id>/archive', views.archive_article, name='archive_article'),
    path('<str:username>/board/<int:board_id>/article/<int:article_id>/restore', views.restore_article, name='restore_article'),
]
