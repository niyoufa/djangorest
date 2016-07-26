# -*- coding: utf-8 -*-
from rr_manage.models import (
                            Area, Version, Legalservice, Certificate, Ordertype, Reporttype, 
                            Skilledfield, Comments, Park, Bank, Indexpic,Tags
                            )
from rr_user.models import User
from rr_user.serializers import UserSerializer
from rr_manage.serializers import (ParkSerializer, CertificateSerializer, VersionSerializer, 
                                   BusinessSerializer, CommentsSerializer,UsermapSerializer,ParkmapSerializer,
                                   OrdertypeSerializer, BankSerializer, IndexpicSerializer,TagsSerializer)
from rest_framework import generics,status,filters
from django.db.models import Q,F
from drf_multiple_model.views import MultipleModelAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from map import getlocation
from map.getdistance import *
from django.core.context_processors import request
import datetime

class ReviewTagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.filter(type=1)
    serializer_class = TagsSerializer 
      
class ParkTagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.filter(type=2)
    serializer_class = TagsSerializer   
    
class ParkList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Park.objects.all()
        city = self.request.query_params.get('city__startswith', None)
        if city:
            queryset = queryset.filter(city__startswith=city)
        return queryset
    serializer_class = ParkSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id','city','area','type')
    ordering_fields = '__all__'
    
    def get(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        lis = serializer.data
        try:
            p1 = Point()
            p1.lat = float(request.GET.get('lat').encode("utf-8"))
            p1.lng = float(request.GET.get('lng').encode("utf-8"))
            for i in lis:
                p2 = Point()
                try:
                    p2.lat = float(i.get("latitude").encode("utf-8"))
                    p2.lng = float(i.get("longitude").encode("utf-8"))
                except:
                    p2.lat = p1.lat
                    p2.lng = p1.lng
                i['distance']=getDistance(p1, p2)
        except:
            pass
        ordering=self.request.query_params.get('ordering', None)
        if ordering is None or ordering=="distance":
            try:
                lis = sorted(serializer.data, key=lambda s: s['distance'])  
            except:
                pass      
        if request.GET.get('limit'):
            limit = int(request.GET['limit'])
            if request.GET.get('offset'):
                offset = int(request.GET['offset'])
            else:
                offset = 0
            return self.get_paginated_response(lis[offset:offset+limit])    
        return Response(lis)  
class ParkDetail(generics.RetrieveAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    
#######################################################################################            
class CertificateL(generics.ListAPIView):
    queryset = Certificate.objects.filter(status='1')
    serializer_class = CertificateSerializer  
#######################################################################################            
    
class BusinessList(generics.ListAPIView):
    queryset = Skilledfield.objects.filter(status='1')
    serializer_class = BusinessSerializer   
 

 
#######################################################################################            
class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    def post(self, request, *args, **kwargs):
        request.data["createtime"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.create(request, *args, **kwargs)
 
#######################################################################################   

class NewVersion(APIView):   
    def get(self, request, format=None):
        version = Version.objects.all()[0]
        serializer = VersionSerializer(version)
        return Response(serializer.data)
#######################################################################################
class OrdertypeDetail(generics.RetrieveAPIView):        
    queryset = Ordertype.objects.filter(status='1')
    serializer_class = OrdertypeSerializer 
#######################################################################################
class BankList(generics.ListCreateAPIView):   
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('bank','id')     
    def get_queryset(self):
        queryset = Bank.objects.values('bank').distinct()
        bank = self.request.query_params.get('bank', None)
        if bank:
            queryset = Bank.objects.values('id','branch')
        return queryset
    serializer_class = BankSerializer
#######################################################################################
class Indexpicture(generics.ListAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()         
    queryset = Indexpic.objects.filter(isused=1)
    serializer_class = IndexpicSerializer  