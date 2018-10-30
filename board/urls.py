from django.urls import path

from . import views


urlpatterns = [
    path('', views.studentHome, name='studentHome'),
    path('studentArchived', views.studentArchived, name='studentArchived'),
    path('teacherHome', views.teacherHome, name='teacherHome'),
]
