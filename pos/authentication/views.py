from django.shortcuts import render
from rest_framework import generics, status , views
from coachingapi.serilizers import RegisterSerializer, EmailVerificationSerialize, LoginSerilizer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import User
from authentication.utils import Util 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# Create your views here.
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username+' Use below link to verify.\n'+absurl
        data = {'email_body': email_body,'to_email' : user.email, 'email_subject':'Very your email', }
        Util.send_email(data)

        return Response(user_data, status = status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerialize
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters = [token_param_config])
    def get(self,request):
        token = request.GET.get('token')        
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'email':'Successfully activated'}, status= status.HTTP_200_OK)
        except jwt.ExpiredSignature as identifier:
            return Response({'error':'Activation token expired'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid tooken'}, status= status.HTTP_400_BAD_REQUEST)
            
class LoginApiView(generics.GenericAPIView)        :

    serializer_class = LoginSerilizer
    def post(self, request):
        serilizer = self.serializer_class(data = request.data)
        serilizer.is_valid(raise_exception = True)
        return Response(serilizer.data, status=status.HTTP_200_OK)