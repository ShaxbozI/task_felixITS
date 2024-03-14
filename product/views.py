from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import *
from .serializers import (
    ProductSerializer,
    ProductMaterialsSerializer,
    MaterialsCountSerializer,
    UnitysSerializer
)



# Mahsulotni yaratish 
class ProductView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ProductSerializer
    
    
    
    
# Mahsulot uchun material yaratish 
class ProductMaterialsView(CreateAPIView):
    queryset = ProductMaterials.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ProductMaterialsSerializer
    
    
    
    
# Mahsulot xomashyolarining birligi yaratish 
class UnitysView(CreateAPIView):
    queryset = Unitys.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UnitysSerializer
    
    
    
    
# Mahsulot uchun ishlatiladian material hamda uning qiymati va narhini kiritish 
class MaterialsCountView(CreateAPIView):
    queryset = MaterialsCount.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = MaterialsCountSerializer






    
    
