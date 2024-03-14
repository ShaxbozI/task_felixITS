from django.db import models

from product.models import ProductMaterials




# Xomashyoning ombordagi miqdori yoki soni hamda narxi
class Warehouse(models.Model):
    material = models.ForeignKey(ProductMaterials, on_delete=models.CASCADE)
    remainder = models.FloatField()
    price = models.FloatField()
    
    def __str__(self) -> str:
        return self.material.material_name