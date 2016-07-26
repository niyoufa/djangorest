# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rr_manage import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^park/$', views.ParkList.as_view()),
    url(r'^park/(?P<pk>[0-9]+)/$', views.ParkDetail.as_view()),
#     url(r'^park/review/$', views.ReviewList.as_view()),
#     url(r'^park/review/(?P<pk>[0-9]+)/$', views.ServiceReview.as_view()),
    
    url(r'^certificate/$', views.CertificateL.as_view()),  
    
#     url(r'^rate/(?P<tax>[0-9]+)/$', views.RateList.as_view()),  
#     url(r'^rate/(?P<tax>[0-9]+)/(?P<invoice>[0-9]+)/$', views.RateList.as_view()),
    url(r'^business/$', views.BusinessList.as_view()),  
    url(r'^reviewtags/$', views.ReviewTagsList.as_view()),  
    url(r'^parktags/$', views.ParkTagsList.as_view()),  
#     
    url(r'^comments/$', views.CommentsList.as_view()), 
    
    url(r'^version/$', views.NewVersion.as_view()), 
    url(r'^indexpic/$', views.Indexpicture.as_view()), 
    url(r'^servicecon/(?P<pk>[0-9]+)/$', views.OrdertypeDetail.as_view()),
    url(r'^bank/$', views.BankList.as_view()), 
]


urlpatterns = format_suffix_patterns(urlpatterns)