from django.urls import path
from .views import *

urlpatterns = [
    path('', WarehoseCountView.as_view(), name='count_product'),
    path('warehouse/material/', WarehouseProductView.as_view(), name='warehouse_material'),
]