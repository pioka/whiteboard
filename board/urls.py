from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/board/<int:board_id>/', views.list_articles, name='list_articles'),
    path('<str:username>/board/<int:board_id>/settings', views.list_articles, name='board_settings'),
    path('<str:username>/board/<int:board_id>/create_article', views.create_article, name='create_article')
]
