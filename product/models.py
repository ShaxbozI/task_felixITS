from django.db import models



# Xomashtolar
class ProductMaterials(models.Model):
    material_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.material_name
    
    class Meta:
        verbose_name = 'Product Materials'
        verbose_name_plural = 'Product Materials'
    

# Mahsulotlar
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.product_name


# Xomashyoning ombordagi miqdorining birligi
class Unitys(models.Model):
    unity = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.unity
    
    class Meta:
        verbose_name = 'Unitys'
        verbose_name_plural = 'Unitys'
    

# Mahsulot uchun ishlatiladigan xomashyo va 1 dona mahsulot uchun qancha yoki nechta xomashyo ishlatilishi
class MaterialsCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    materials = models.ForeignKey(ProductMaterials, on_delete=models.CASCADE)
    count = models.FloatField()
    count_unity = models.ForeignKey(Unitys, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.product.product_name}: {self.materials.material_name} xomashyosi"
    

