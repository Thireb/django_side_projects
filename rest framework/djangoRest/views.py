from webbrowser import get
from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response


class testApi(APIView):
    def get(self,request,*args, **kwargs):
        data = {
            'username':'Ahmad',
            'age':22
        }
        return Response(data)