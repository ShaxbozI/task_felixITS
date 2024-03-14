from rest_framework import serializers

from .models import Warehouse
from product.models import ProductMaterials, Product



# Mavjud xom-ashyolarning ombordagi narxi va miqdorini kiritish uchun serializer
class ProductSerializer(serializers.ModelSerializer):
    material = serializers.PrimaryKeyRelatedField(queryset=ProductMaterials.objects.all(), required=True)
    class Meta:
        model = Warehouse
        fields = ['id', 'material', 'remainder', 'price']

    def create(self, validated_data):
        info = Warehouse.objects.create(**validated_data)
        return info
    
    
    
# Mahsulot uchun ombordagi xomashyolarni hisoblash request yuborsh uchun serializer 
# Bu modelga bog'liq emas 
class WarehouseCountSerializer(serializers.Serializer):
    product_name = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=True)
    product_qty = serializers.CharField(max_length=11)


# Bir nechta mahsulotni bir vaqtda kiritish uchun serializer
class WarehouseCounListtSerializer(serializers.Serializer):
    product_list = serializers.ListField(child=WarehouseCountSerializer())
    
    
    
