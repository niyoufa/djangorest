# -*- coding: utf-8 -*-
from rr_user.models import User
from register import run
from rest_framework import generics,filters,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import datetime, random, string
from register.models import Coupons
from register.serializers import CouponsSerializer
from rest_auth.serializers import PasswordChangeSerializer
from django.db.models import Q
from DjangoCaptcha import Captcha
from django.http import HttpResponse

class CouponsList(generics.ListCreateAPIView):
    queryset = Coupons.objects.all()
    serializer_class = CouponsSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('phone','status')
    ordering_fields = '__all__'
    def get_queryset(self):
        today=datetime.date.today().strftime("%Y-%m-%d")
        queryset = Coupons.objects.filter(Q(status='') | Q(status='1'),endtime__gte=today)
        return queryset
    def post(self, request, *args, **kwargs):
        if request.data.get("phone"):
            try:
                Coupons.objects.get(phone=request.data["phone"])
                return Response("已领取")
            except Coupons.DoesNotExist:
                obj = '%05d' % random.randint(0,99999)
                while (len(obj) < 8):  
                    obj+=random.choice(string.ascii_uppercase) 
                request.data["number"]=obj
                today = datetime.date.today()
                year=(today.month+2)/12+today.year
                month=(today.month+2)%12+1
                request.data["starttime"]=today.strftime("%Y-%m-%d")
                request.data["endtime"]="%s-%02d-%02d"%(year,month,today.day)
                request.data["status"]='1'
                request.data["createtime"]=request.data["modifytime"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result = self.create(request, *args, **kwargs)
                if str(request.data.get("sendmsg"))=='1':
                    content = {'code':obj}
                    mobile = request.data["phone"]
                    run.aliyun_sendmsg(mobile, 1305, **content)
                return result
class CouponsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupons.objects.all()
    serializer_class = CouponsSerializer
    lookup_field = 'number'
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            return queryset.get(id=self.kwargs.get('number'))
        except:
            return super(CouponsDetail, self).get_object()
    def put(self, request, *args, **kwargs):
        if request.data.get('status'):
            instance = self.get_object()
            coupons=Coupons.objects.get(id=instance.id)
            coupons.status=request.data.get('status')
            coupons.save()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if request.data.get('status'):
            instance = self.get_object()
            coupons=Coupons.objects.get(id=instance.id)
            coupons.status=request.data.get('status')
            coupons.save()
        return self.partial_update(request, *args, **kwargs)
    
class Sendcode(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = ()
    def post(self, request, *args, **kwargs):
        params = request.data
        mobile = params.get('mobile')
        usertype = params.get('type')
        domain = params.get('domain')
        if mobile is not None:
            if usertype=='b' or usertype=='c':
                try:
                    User.objects.get(username="%s_%s"%(mobile,usertype))
                except User.DoesNotExist:
                    return Response('用户不存在')
                else:
                    req =run.aliyun_sendcode(mobile,domain)
                    return Response(req)
            else:
                try:
                    if domain[-1]=="c":
                        User.objects.get(username="%s_c"%mobile)
                    else:
                        User.objects.get(username="%s_b"%mobile)
                except User.DoesNotExist:
                    req =run.aliyun_sendcode(mobile,domain)
                    return Response(req)
                else:
                    return Response('该手机号已注册')              
        return Response(params)
class Checkcode(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = () 
    def post(self, request, *args, **kwargs):
        params = request.data
        if params.get('mobile'):
            mobile=params.get('mobile')
            code =params.get('code')
            domain = params.get('domain')
            req =run.aliyun_checkcode(mobile, code, domain)
            return Response(req)
        return Response(params)
    
class Changepassword(generics.GenericAPIView):  
    permission_classes = (AllowAny,)
    authentication_classes = () 
    serializer_class = PasswordChangeSerializer
    def post(self, request, *args, **kwargs):
        params = request.DATA
        username = params.pop('username',None)
        params['new_password1'] = params['new_password2'] = params.pop('new_password',None)
        code = params.pop('code',None)
        domain = params.pop('domain',None)
        if username.endswith(('_b','_c')):
            mobile=username[:-2]
            req =run.aliyun_checkcode(mobile, code, domain)
            result = req['open_sms_checkvercode_response']['result']['successful']
            if result is True:
                request.user = User.objects.get(username=username)
                serializer = self.get_serializer(data=params)
                if not serializer.is_valid():
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
                serializer.save()
                return Response({"success": "New password has been saved."})
            return Response({"fail": "code is Error!"})
        return Response(params) 

def piccode(request):
    ca =  Captcha(request)
    ca.type = 'number'
    return ca.display()

class Checkpiccode(APIView):  
    permission_classes = (AllowAny,)
    authentication_classes = ()
    def get(self, request, *args, **kwargs):
        params = self.request.query_params
        mobile = params.get('mobile')
        usertype = params.get('type')
        domain = params.get('domain')
        _code = params.get('code') or ''
        ca = Captcha(request)
        if ca.validate(_code):
            if mobile is not None:
                if usertype=='b' or usertype=='c':
                    try:
                        User.objects.get(username="%s_%s"%(mobile,usertype))
                    except User.DoesNotExist:
                        return Response('用户不存在')
                    else:
                        req =run.aliyun_sendcode(mobile,domain)
                        return Response(req)
                else:
                    try:
                        if domain[-1]=="c":
                            User.objects.get(username="%s_c"%mobile)
                        else:
                            User.objects.get(username="%s_b"%mobile)
                    except User.DoesNotExist:
                        req =run.aliyun_sendcode(mobile,domain)
                        return Response(req)
                    else:
                        return Response('该手机号已注册') 
            return Response('手机号不能为空')              
        return Response('验证码错误')
# def index(request):
#     _code = request.GET.get('code') or ''
#     ca = Captcha(request)
#     if ca.validate(_code):
#         return HttpResponse("""ok""")
#     return HttpResponse("""error""")
