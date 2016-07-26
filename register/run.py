# -*- coding: utf-8 -*-
from xlrd import open_workbook
from rr_user.models import User
from rr_manage.models import Certificate
import urllib, urllib2, json
from map import getlocation
from django.conf import settings
import top.api

sexdict={u'男':'1',u'女':'2'}
taxpayerstypedict={u'一般纳税人':'0',u'小规模纳税人':'1'}

def signup(username,email=None):
    host=settings.DATABASES['default']['HOST']
    url = 'http://'+host+':8100/rest-auth/registration/'
    values = {'username':username,
              'password1':'123456',
              'password2':'123456'}
    if email:
        values['email']=email
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def sendmsg(content,mobile):
    url = 'http://115.29.170.211:8011/sms.aspx/'
    params = ({'mobile':mobile,'content':content,'sendTime':'','extno':''})
    data='action=send&userid=756&account=2017003&password=aa123321&'+urllib.urlencode(params)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def aliyun_sendmsg(mobile,template_id,**context):
    top.setDefaultAppInfo("23235698", "613d69c00f1f3980ed0f9df81be1369a")
    req=top.api.OpenSmsSendmsgRequest()
    params = {"mobile":mobile,"signature_id":31,"template_id":template_id,"context":context}
    req.send_message_request=json.dumps(params)
    try:
        resp= req.getResponse()
        return resp
    except Exception,e:
        return e
    
def aliyun_sendcode(mobile,domain=None):
    top.setDefaultAppInfo("23235698", "613d69c00f1f3980ed0f9df81be1369a")
    req=top.api.OpenSmsSendvercodeRequest()
    params = {"mobile":mobile,"signature_id":31,"template_id":310921775,"expire_time":600,
              "ver_code_length":4,"context":{'minute':10},"domain":domain}
    req.send_ver_code_request=json.dumps(params)
    try:
        resp= req.getResponse()
        return resp
    except Exception,e:
        return e
    
def aliyun_checkcode(mobile,code,domain=None):
    top.setDefaultAppInfo("23235698", "613d69c00f1f3980ed0f9df81be1369a")
    req=top.api.OpenSmsCheckvercodeRequest()
    params = {"mobile":mobile,"ver_code":code,"check_success_limit":2,"domain":domain}
    req.check_ver_code_request=json.dumps(params)
    try:
        resp= req.getResponse()
        return resp
    except Exception,e:
        return e

