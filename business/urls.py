# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from business import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^personnelinf/$', views.PersonnelinfList.as_view()),
    url(r'^personnelinf/(?P<pk>[0-9]+)/$', views.PersonnelinfDetail.as_view()),
    url(r'^personnelinf/user/(?P<pk>[0-9]+)/$', views.UserpersonnelinfList.as_view()), 
    
    url(r'^lawinfship/(?P<pk>[0-9]+)/$', views.LawinfshipDetail.as_view()),           
               
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^order/user/(?P<pk>[a-z 0-9]+)/$', views.Userorder.as_view()),
    url(r'^childorder/(?P<pk>[0-9]+)/$', views.ChildOrderDetail.as_view()),
    url(r'^childorder/user/(?P<pk>[0-9]+)/$', views.Userchildorder.as_view()),    
    url(r'^recentorder/user/(?P<pk>[0-9]+)/$', views.Userrecentorder.as_view()),   
    url(r'^applyInvoiceorder/(?P<pk>[0-9]+)/$', views.applyInvoiceorder.as_view()),
    url(r'^user/review/$', views.ReviewList.as_view()),
    url(r'^user/review/(?P<pk>[0-9]+)/$', views.ServiceReview.as_view()),    
]

urlpatterns += [
    url(r'^balancesheet/$', views.BalancesheetList.as_view()),
    url(r'^allsheet/(?P<period>[0-9]+)/$', views.AllsheetList.as_view()),
    url(r'^express/$', views.ExpressList.as_view()),
    url(r'^express/(?P<pk>[0-9]+)/$', views.ExpressDetail.as_view()),
    url(r'^express/user/(?P<pk>[a-z 0-9]+)/$', views.Userexpress.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
