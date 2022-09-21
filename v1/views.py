from django.shortcuts import render

from .models import *
from .serializers import *

from django.http import JsonResponse, HttpResponse, Http404

from rest_framework.response import Response
from rest_framework import status






# Create your views here.



############### Function Based View ################
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse, Http404

from rest_framework.response import Response
from rest_framework import status

#@csrf_exempt
@api_view(['GET','POST'])
def CategoriesView(request):
    if request.method == "GET":
        queryset = Category.objects.all()
        ser = CategorySerializer(queryset, many=True)
        #return JsonResponse(ser.data,safe=False,status=200)
        #return HttpResponse(ser.data, content_type='application/json')
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        ser = CategorySerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def CategoryView(request,id):
    try:
        queryset = Category.objects.get(id=id)
    except:
        raise Http404
    if request.method == "GET":
        ser = CategorySerializer(queryset)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data
        ser = CategorySerializer(queryset,data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




############# Class Based View ##############
##from rest_framework.views import APIView
##from rest_framework.response import Response
##from rest_framework import status

##
##class ProductsView(APIView):
##    def get(self,resuest):
##        queryset = Product.objects.filter(is_active=True)
##        ser = Product_Serializer(queryset, many=True)
##        return Response(ser.data,status=status.HTTP_200_OK)
##    def post(self,request):
##        data = request.data
##        ser = Product_Serializer(data=data)
##        if ser.is_valid():
##            ser.save()
##            return Response(ser.data,status=status.HTTP_201_CREATED)
##        return Response(status=status.HTTP_400_BAD_REQUEST)
##
##
##class ProductView(APIView):
##    def get_obj(self,id):
##        try:
##            return Product.objects.get(id=id)
##        except:
##            raise Http404
##    def get(self,request,id):
##        queryset = self.get_obj(id)
##        ser = Product_Serializer(queryset)
##        return Response(ser.data,status=status.HTTP_200_OK)
##    def put(self,request,id):
##        queryset = self.get_obj(id)
##        data = request.data
##        ser = Product_Serializer(queryset,data=data)
##        if ser.is_valid():
##            ser.save()
##            return Response(ser.data,status=status.HTTP_201_CREATED)
##        return Response(status=status.HTTP_400_BAD_REQUEST)
##    def delete(self,request,id):
##        queryset = self.get_obj(id)
##        queryset.delete()
##        return Response(status=status.HTTP_204_NO_CONTENT)
##
##
##
##
########### Class Based View ##############
########### Mixing ############
##from rest_framework import mixins
##from rest_framework import generics
##
##
##class ProductsView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
##    queryset = Product.objects.filter(is_active=True)
##    serializer_class = Product_Serializer
##    def get(self,request, *args, **kwargs):
##        return self.list(request, *args, **kwargs)
##    def post(self, request, *args, **kwargs):
##        return self.create(request, *args, **kwargs)
##
##
##class ProductView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
##    queryset = Product.objects.filter(is_active=True)
##    serializer_class = Product_Serializer
##    def get(self,request, *args, **kwargs):
##        return self.retrieve(request, *args, **kwargs)
##    def put(self, request, *args, **kwargs):
##        return self.update(request, *args, **kwargs)
##    def delete(self, request, *args, **kwargs):
##        return self.destroy(request, *args, **kwargs)
##
##
############# Class Based View ##############
############# Generic ############
from rest_framework import generics


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = Product_Serializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = Product_Serializer