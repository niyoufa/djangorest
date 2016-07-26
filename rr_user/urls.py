# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rr_user import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^expressadd/$', views.ExpressaddList.as_view()),
    url(r'^expressadd/(?P<pk>[0-9]+)/$', views.ExpressaddDetail.as_view()),
    url(r'^expressadd/user/(?P<pk>[a-z 0-9]+)/$', views.Userexpressadd.as_view()),
             
    url(r'^workexp/$', views.WorkexperienceList.as_view()),
    url(r'^workexp/(?P<pk>[0-9]+)/$', views.WorkexperienceDetail.as_view()),
    url(r'^workexp/user/(?P<pk>[a-z 0-9]+)/$', views.Userworkexperience.as_view()),
            

    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^financeuser/(?P<pk>[0-9]+)/$', views.FinanceuserDetail.as_view()),
    url(r'^user/search/$', views.UserSearch.as_view()),
    url(r'^user/userkey/(?P<mobile>[a-z 0-9_]+)/$', views.UserKey.as_view()),
    
    url(r'^company/$', views.CompanyList.as_view()),
    url(r'^company/(?P<pk>[0-9]+)/(?P<user>[0-9]+)/$', views.CompanyDelete.as_view()),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
    url(r'^company/user/(?P<user>[0-9]+)/$', views.ServiceCompanyList.as_view()),
#     url(r'^price/$', views.PriceList.as_view()),
#     url(r'^price/(?P<pk>[0-9]+)/$', views.PriceDetail.as_view()),
    url(r'^price/user/(?P<user>[0-9]+)/$', views.ServicePrice.as_view()),
#     
    url(r'^withdrawal/$', views.WithdrawalList.as_view()),
#     url(r'^withdrawal/(?P<pk>[0-9]+)/$', views.WithdrawalDetail.as_view()),
    url(r'^withdrawal/user/(?P<user>[0-9]+)/$', views.ServiceWithdrawal.as_view()),
    url(r'^withdrawal/userdetail/(?P<pk>[0-9]+)/$', views.UserWithdrawalDetail.as_view()),
    
    url(r'^user/report/$', views.ServiceReportList.as_view()),
    url(r'^user/report/(?P<user>[0-9]+)/$', views.ServiceReport.as_view()),
#     url(r'^user/orderstatus/(?P<user>[0-9]+)/$', views.Orderstatus.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
