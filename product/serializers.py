from rest_framework import serializers

from .models import ProductMaterials, Product, MaterialsCount, Unitys



# Mahsulot qo'shish serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name']

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product



# Xom-ashyo qo'shish serializer
class ProductMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterials
        fields = ['id', 'material_name']

    def create(self, validated_data):
        material = ProductMaterials.objects.create(**validated_data)
        return material



# Xom-ashyo uchun birlik qo'shish serializer
class UnitysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unitys
        fields = ['id', 'unity']

    def create(self, validated_data):
        unity = Unitys.objects.create(**validated_data)
        return unity
    
    
 
# 1-dona Mahsulot uchun xom-ashyo hamda narxi va miqdorini qo'shish serializer
class MaterialsCountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=True)
    materials = serializers.PrimaryKeyRelatedField(queryset=ProductMaterials.objects.all(), required=True)
    count_unity = serializers.PrimaryKeyRelatedField(queryset=Unitys.objects.all(), required=True)
    class Meta:
        model = MaterialsCount
        fields = ['id', 'product', 'materials', 'count', 'count_unity']

    def create(self, validated_data):
        material_couny = MaterialsCount.objects.create(**validated_data)
        return material_couny
