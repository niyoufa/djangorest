# -*- coding: utf-8 -*-
from django.conf.urls import url
from pay import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.create_direct_pay, name="payment_upgrade_account"),
    url(r'^success/$', TemplateView.as_view(template_name='pay/success.html'), name="pay_success"),
    url(r'^error/$', TemplateView.as_view(template_name='pay/error.html'), name="pay_error"),
    url(r'^notify/$', views.notify, name="notify_url"),
    url(r'^(?P<payway>[a-z]+)notify/$', views.notify, name="wxnotify_url"),
    url(r'^jspay/$', views.jspay),
    url(r'^jspay/test.html$', views.paytest),
    url(r'^jspay/b$', views.paytestb),
]


urlpatterns = format_suffix_patterns(urlpatterns)