# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from community import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^article/$', views.ArticleList.as_view()),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^article/comments/$', views.CommentsList.as_view()),
    url(r'^article/complaint/$', views.ComplaintsList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)