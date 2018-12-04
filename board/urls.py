from django.urls import path

from . import views


urlpatterns = [
    path('board', views.index, name='index'),
    path('board/<int:board_id>', views.list_articles, name='list_articles'),
    path('board/<int:board_id>/settings', views.list_articles, name='list_articles'),
    path('board/<int:board_id>/create_article', views.create_article, name='create_article')
]
