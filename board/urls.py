from django.urls import path

from . import views


urlpatterns = [
    path('', views.studentHome, name='studentHome'),
    path('teacherHome', views.teacherHome, name='teacherHome'),
    path('teacherCreateArticle', views.teacherCreateArticle, name='teacherCreateArticle')
]
