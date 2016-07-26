# -*- coding: utf-8 -*-
import os, json
import datetime
from aliyun_oss.conf import oss,bucket
from aliyun_oss.forms import UploadImg,size
from django.http import HttpResponse
from PIL import Image
from rr_user.models import User,Financeuser
from community.models import Picture
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# Create your views here.
class Register(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = () 
    def post(self, request, *args, **kwargs):
        form = UploadImg(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            lte=data["img"].name.split('.')[-1]
            img=Image.open(data["img"])
            user = User.objects.get(id=data['pk'])
            if user.type=='c':
                financeuser = Financeuser.objects.get(id=data['pk'])
            if data['obj']=='user':
                if data['type']=='icon':
                    w = img.size[0]
                    h = img.size[1]
                    l = size(w,h)
                    img=img.transform((l[0],l[0]),Image.EXTENT,l[1])
                    if l[0]>300:
                        img.thumbnail((300, 300)) 
                objectname = "user_%s_%s.%s"%(data['pk'],data['type'],lte)
                objectname_min = "user_%s_%s_50*50.%s"%(data['pk'],data['type'],lte)
                img.save("/home/renren/renren_bo/static/%s"%objectname)
                img.thumbnail((50, 50))
                img.save("/home/renren/renren_bo/static/%s"%objectname_min)
                oss.put_object_from_file(bucket, objectname, "/home/renren/renren_bo/static/%s"%objectname)
                oss.put_object_from_file(bucket, objectname_min, "/home/renren/renren_bo/static/%s"%objectname_min)
                url='http://%s.oss-cn-hangzhou.aliyuncs.com/%s'%(bucket,objectname)
                url_min='http://%s.oss-cn-hangzhou.aliyuncs.com/%s'%(bucket,objectname_min)
#                 d={data['type']:url}
                if data['type']=='icon':
                    user.iconPath=url
                    user.save()
                elif data['type'] in ['idcardimg','idcardimg_opp']:
                    path = financeuser.idcardimgpath.split(',') if financeuser.idcardimgpath else [url]
                    for i in range(len(path)):
                        if '%s.'%data['type'] in path[i]:
                            path[i]=url
                            break
                        path.append(url)
                    financeuser.idcardimgpath = ','.join(path)
                    financeuser.save()
                elif data['type'] in ['accountantimg','accountantimg_opp']:
                    path = financeuser.accountantimgpath.split(',') if financeuser.accountantimgpath else [url]
                    for i in range(len(path)):
                        if '%s.'%data['type'] in path[i]:
                            path[i]=url
                            break
                        path.append(url)
                    financeuser.accountantimgpath = ','.join(path)
                    financeuser.save()
                elif data['type'] in ['certificateimg','certificateimg_opp']:
                    path = financeuser.certificateimgpath.split(',') if financeuser.certificateimgpath else [url]
                    for i in range(len(path)):
                        if '%s.'%data['type'] in path[i]:
                            path[i]=url
                            break
                        path.append(url)
                    financeuser.certificateimgpath = ','.join(path)
                    financeuser.save()
                os.remove("/home/renren/renren_bo/static/%s"%objectname)
                os.remove("/home/renren/renren_bo/static/%s"%objectname_min)
                return HttpResponse(url_min)
            elif data['obj']=='picture':
                dt = datetime.datetime.now()
                objectname = "picture_%s_%s.%s"%(data['pk'],dt.strftime('%y%m%d%H%M%S%f'),lte)
                img.save("/home/renren/renren_bo/static/%s"%objectname)
                res = oss.put_object_from_file(bucket, objectname, "/home/renren/renren_bo/static/%s"%objectname)
                url='http://%s.oss-cn-hangzhou.aliyuncs.com/%s'%(bucket,objectname)
                p = Picture.objects.create(user=user.id,image=url)
                os.remove("/home/renren/renren_bo/static/%s"%objectname)
                d={'id':p.id,'url':url}
                return HttpResponse(json.dumps(d))
    