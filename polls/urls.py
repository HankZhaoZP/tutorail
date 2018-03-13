# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:33
# @Author  : HankZhao
# @File    : urls.py
# @Describe:


from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.result, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]