from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView
."""

    def get(self,request,format=None):

        an_apiview = [
            'item number 1',
            'item number 2',
            'item number 3'
        ]

        return Response({'message':'Hello', 'an_apiview' : an_apiview})
