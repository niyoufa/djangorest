# -*- coding: utf-8 -*-
from django.conf.urls import url
from register import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
#     url(r'^sendcode/$', views.Sendcode.as_view()),
    url(r'^rios/sendcode/$', views.Sendcode.as_view()),
    url(r'^rios/sendcode/$', views.Sendcode.as_view()),
    url(r'^checkpiccode/$',views.Checkpiccode.as_view()),
    url(r'^piccode/$',views.piccode),
    url(r'^checkcode/$', views.Checkcode.as_view()),
    url(r'^changepassword/$', views.Changepassword.as_view()),
    url(r'^coupons/$', views.CouponsList.as_view()),
    url(r'^coupons/(?P<number>[\s\S]+)/$', views.CouponsDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)