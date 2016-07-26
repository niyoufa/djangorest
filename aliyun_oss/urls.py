# -*- coding: utf-8 -*-
from django.conf.urls import url
from aliyun_oss import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^upload/$', views.Register.as_view(), name='upload'),
]