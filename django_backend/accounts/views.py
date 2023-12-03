from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.authentication import TokenAuthentication

from .models import *
from .serializers import *
from accounts.models import *

# Create your views here.

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username


#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'PUT'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def user_profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        print(user)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)