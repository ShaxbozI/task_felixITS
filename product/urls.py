from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='add_product'),
    path('material/', ProductMaterialsView.as_view(), name='add_material'),
    path('unity/', UnitysView.as_view(), name='add_unity'),
    path('one/pro/material/', MaterialsCountView.as_view(), name='add_unity'),
]