# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics
from community.models import Picture, Article, Comments, Complaints, Article_images
from community.serializers import PictureSerializer,ArticleSerializer,CommentsSerializer,ComplaintsSerializer
import datetime

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now
        ret=self.create(request, *args, **kwargs)
        if request.data.get("images"):
            for i in request.data.get("images"):
                Article_images.objects.get_or_create(articleid=ret.data['id'],pictureid=i)
        return ret

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentsList(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now
        return generics.CreateAPIView.post(self, request, *args, **kwargs)
    
class ComplaintsList(generics.ListCreateAPIView):
    queryset = Complaints.objects.filter(isread='0')
    serializer_class = ComplaintsSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now
        return generics.ListCreateAPIView.post(self, request, *args, **kwargs)