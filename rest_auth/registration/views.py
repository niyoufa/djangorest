from django.contrib.auth import login, logout
from django.conf import settings
from rr_user.models import Financeuser
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from allauth.account.views import SignupView, ConfirmEmailView
from allauth.account.utils import complete_signup
from allauth.account import app_settings
from rest_auth.app_settings import UserDetailsSerializer
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.views import Login
from rest_auth.serializers import jwt_response_payload_handler
from rest_framework_jwt.settings import api_settings
from datetime import datetime

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER




class Register(APIView, SignupView):

    permission_classes = (AllowAny,)
    authentication_classes = () 
    user_serializer_class = UserDetailsSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def form_valid(self, form):
        self.user = form.save(self.request)
        if isinstance(self.request, HttpRequest):
            request = self.request
        else:
            request = self.request._request
        return complete_signup(request, self.user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())

    def login(self):
        self.token, created = Login.token_model.objects.get_or_create(
            user=self.user)
        if self.user.type=='c':
            Financeuser.objects.get_or_create(id=self.user.id, isacceptorder='1')
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)
            
    def post(self, request, *args, **kwargs):
        self.initial = {}
        self.request.POST = self.request.DATA.copy()
        if request.POST.get("username") is None:
            self.request.POST["username"]="%s_%s"%(request.POST.get("phone"),request.POST.get("type"))
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        if self.form.is_valid():
            self.form_valid(self.form)
            self.user.phone=request.POST["username"][:-2]
            self.user.type=request.POST["username"][-1:]
            self.user.channel=request.POST.get("channel")
            self.user.createTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.user.save()
            self.login()
            return self.get_response2()
        else:
            return self.get_response_with_errors()

    def get_response(self):
        serializer = self.user_serializer_class(instance=self.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get_response2(self):
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)
        response_data = jwt_response_payload_handler(token, self.user)
        return Response(response_data, status=status.HTTP_201_CREATED)
    def get_response_with_errors(self):
        return Response(self.form.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView, ConfirmEmailView):

    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get(self, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        self.kwargs['key'] = self.request.DATA.get('key', '')
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)


class SocialLogin(Login):
    """
    class used for social authentications
    example usage for facebook

    from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
    class FacebookLogin(SocialLogin):
        adapter_class = FacebookOAuth2Adapter
    """

    serializer_class = SocialLoginSerializer
