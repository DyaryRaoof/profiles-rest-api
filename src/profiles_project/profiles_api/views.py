from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models


# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView
."""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiview = [
            'item number 1',
            'item number 2',
            'item number 3'
        ]

        return Response({'message':'Hello', 'an_apiview' : an_apiview})

    def post(self,request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        return Response({'method':'put'})


    def patch(self,request,pk=None):
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset = [
    'viewset list item no 1',
    'viewset list item no 2',
    'viewset list item no 3',
    ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})


    def create(self,request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message' : message, 'name' : name})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self,request,pk=None):
        return Response({'http_method': 'Get'})


    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        return Response({'http_method': 'PATCH'})


    def destroy(self,request,pk=None):
        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
