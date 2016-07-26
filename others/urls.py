# -*- coding: utf-8 -*-
from django.conf.urls import url
from others import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^news/$', views.NewsList.as_view()),
    url(r'^news/id/(?P<pk>[0-9]+)/$', views.NewsDetail.as_view()),
    url(r'^news/(?P<pk>[0-9]+)/$', views.UserNewsList.as_view()),
    url(r'^news/noreadnum/(?P<user2>[0-9]+)/$', views.Noreadnum.as_view()),
    url(r'^news/(?P<user1>[0-9]+)/(?P<user2>[0-9]+)/$', views.UserNewsDetail.as_view()),
    url(r'^news/type/(?P<type>[0-9]+)/$', views.TypeNewsDetail.as_view()),
    url(r'^news/type/(?P<type>[0-9]+)/(?P<user2>[0-9]+)/$', views.TypeNewsDetail.as_view()),
    url(r'^rong/user_get_token/$', views.User_get_token.as_view()),
    url(r'^rong/user_get_news/$', views.User_get_news.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)