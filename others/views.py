# -*- coding: utf-8 -*-
from others.models import News
from others.serializers import NewsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
import datetime, time
from others.conf import api
from rr_user.models import User

class UserNewsList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        queryset = super(UserNewsList, self).get_queryset()
        l=[]
        obj1 = queryset.filter(type='1',user2=self.kwargs.get('pk')).order_by('-createtime').values_list('pk', flat=True)
        if len(obj1)>0:
            obj1=obj1[0]
            l.append(obj1)
        obj2 = queryset.filter(type='2').order_by('-createtime').values_list('pk', flat=True)
        if len(obj2)>0:
            obj2=obj2[0]
            l.append(obj2)
        obj3 = queryset.filter(type='3').order_by('-createtime').values_list('pk', flat=True)
        if len(obj3)>0:
            obj3=obj3[0]
            l.append(obj3)
        list1 = queryset.filter(type='4',user1=self.kwargs.get('pk')).values_list('user2', flat=True)
        list2 = queryset.filter(type='4',user2=self.kwargs.get('pk')).values_list('user1', flat=True)
        l1=[]        
        l1=l1+list(list1)+list(list2)
        l1 = list(set(l1))
        if len(l1)>0:
            for k in l1:
                obj4 = queryset.filter(Q(user1=self.kwargs.get('pk'),user2=k)|Q(user2=self.kwargs.get('pk'),user1=k)).order_by('-createtime').values_list('pk', flat=True)[0]
                l.append(obj4)
        return queryset.filter(pk__in=l).order_by('type','-createtime')  
    def get(self, request, *args, **kwargs):
        request.GET = request.GET.copy()
        request.GET['pk'] = self.kwargs.get('pk')
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now 
        return generics.ListCreateAPIView.post(self, request, *args, **kwargs)

class UserNewsDetail(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    paginate_by = 10  
#     paginate_by_param = 'page_c' 
    
    def get_queryset(self):
        queryset = super(UserNewsDetail, self).get_queryset()
        obj = queryset.filter(Q(user1=self.kwargs.get('user1'),user2=self.kwargs.get('user2'))|
                               Q(user2=self.kwargs.get('user1'),user1=self.kwargs.get('user2'))).order_by('-createtime')
        return obj
    def get(self, request, *args, **kwargs):
        News.objects.filter(user1=self.kwargs.get('user2'),user2=self.kwargs.get('user1')).exclude(isread='1').update(isread='1')
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now 
        return generics.ListCreateAPIView.post(self, request, *args, **kwargs)
    
class TypeNewsDetail(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        queryset = super(TypeNewsDetail, self).get_queryset()
        obj = queryset.filter(Q(user2=self.kwargs.get('user2'))|Q(user2__isnull=True),type=self.kwargs.get('type'))\
        .order_by('-createtime').values_list('pk', flat=True)[:20]
        return queryset.filter(pk__in=list(obj)).order_by('createtime')
    #         ordering = ('-createtime',)
       
class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now 
        return generics.ListCreateAPIView.post(self, request, *args, **kwargs)
        
class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
        
class Noreadnum(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = () 
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(user2=self.kwargs.get('user2')).exclude(isread='1').count()
        return Response(queryset)
    
class User_get_token(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = () 
    def get(self, request, *args, **kwargs):
        token = api.call_api(
        action="/user/getToken",
        params={
            "userId": self.request.query_params.get('userId', None),
            "name":self.request.query_params.get('name', None),
            "portraitUri":self.request.query_params.get('portraitUri', None)
        }
    )
        return Response(token)

class User_get_news(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = () 
    def post(self, request, *args, **kwargs):
        params=[]
        try:
            news=list(request.data)
            for i in range(len(news)):
                try:
                    user=User.objects.get(id=news[i]['targetId'])
                    params.append({'lastNew':news[i]['latestMessage']['text'],'unRead':news[i]['unreadMessageCount'],\
                                   'time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(news[i]['sentTime'])/1000)),\
                                   'id':news[i]['targetId'],'name':user.name,'icon':user.get_icon()})
                except:
                    pass
        except :
            pass
        return Response(params)
    
    