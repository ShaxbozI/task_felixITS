from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 

from .models import Warehouse
from .serializers import ProductSerializer, WarehouseCountSerializer, WarehouseCounListtSerializer
from product.models import ProductMaterials, MaterialsCount




class WarehouseProductView(CreateAPIView):
    queryset = Warehouse.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ProductSerializer
    



class WarehoseCountView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = WarehouseCounListtSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Serializerdan mahsulotlar ro'yxati olish
        soralgan_mahsulotlar = serializer.validated_data['product_list']
        
        # Ombordagi barcha xomashyolar olish
        omborda_mavjud_xomashyolar = Warehouse.objects.all()
        
        # Ombordagi xomashyolar ma'lumotlari listi
        ombor_xomashyolar = [{"name": xomashyo.material.material_name, "remainder": xomashyo.remainder, "warehouse_id": xomashyo.id, "price": xomashyo.price} for xomashyo in omborda_mavjud_xomashyolar]
        
        result = []
        
        # Har bir so'ralgan mahsulot uchun unga kerakli xomashyoni(agar yetarli bo'lsa) ombordan olish
        for mahsulot in soralgan_mahsulotlar:
            # Mahsulotlar uchun bo'sh ro'yxat tayyorlanadi
            product_materials = []  
            
            # So'ralgan Mahsulotning nomi va miqdori olish
            product_name = mahsulot['product_name']
            product_qty = mahsulot['product_qty']
            
            # So'ralgan Mahsulotning nomidan foydalanib xomashyolar ro'yxatini olish
            xomashyo_list = MaterialsCount.objects.filter(product=product_name)
            
            # So'ralgan Mahsulotning xomashyolaridan foydalanib kerakli bo'lgan miqdorlarni hisoblash
            soralgan_xomashyolar = {xomashyo.materials.material_name: xomashyo.count * float(product_qty) for xomashyo in xomashyo_list}
            
            # So'ralgan Mahsulot xomashyolar ro'yhatidan foydalanib ularni ombordagi ro'yhat bilan solishtirib so'ralgan miqdorlarni hisoblash
            for name, count in soralgan_xomashyolar.items():
                
                # Kerakli miqdorga yetganda Siklni to'xtatish uchun xomashyo miqdoridan foydalanamiz
                xomashyo_count = count
                for xomashyo_ombor in ombor_xomashyolar:
                    # Xomashyo nomi solishtirish
                    if xomashyo_ombor["name"] == name:
                        # Kerakli xomashyo miqdori aniqlash 
                        # min(), funksiyasi orqali ombordagi va so'ralgan xomashyolardan kichigini olamiz va qty ga tenglaymiz
                        qoldiq = min(xomashyo_count, xomashyo_ombor["remainder"])
                        
                        # qoldiq - ning 0 ga tengligini tekshirishimiz bizga keraksiz malumotlarni kamaytiradi
                        # omborda mavjud bo'lmagan xomashyolardan ham foydalanishni oldini oladi
                        if qoldiq != 0:
                            # Xomashyo ma'lumotlari ro'yxatga qo'shiladi
                            product_materials.append({
                                "warehouse_id": xomashyo_ombor["warehouse_id"],
                                "material_name": name,
                                "qty": qoldiq,
                                "price": xomashyo_ombor["price"]
                            })
                        # qoldiq - dan foydalanib xomashyo miqdori va ombordagi miqdorni kamaytiramiz
                        # bu bizga kerakli xomashyo miqdori va omborda bir partiyadagi xomashyo qancha qolganini aniqlab beradi
                        xomashyo_count -= qoldiq
                        xomashyo_ombor["remainder"] -= qoldiq
                        if xomashyo_count <= 0:
                            break
                
                # Kerakli partiyadagi xomashyo va miqdor mavjud bo'lmaganda qolgan kerakli xomashyo miqdori uchun qo'shimcha malumot chiqarish
                # bu bizga ushbu xomashyodan qancha yetishmasligini aniqlash uchun kerak bo'ladi
                if xomashyo_count > 0:
                    # Xomashyo mavjud emas, null qiymati qo'shiladi
                    product_materials.append({
                        "warehouse_id": None,
                        "material_name": name,
                        "qty": xomashyo_count,
                        "price": None
                    })
                        
            # Har bir mahsulot uchun natijaviy ro'yxatga qo'shish
            result.append({
                "product_name": f"{product_name}",
                "product_qty": f"{product_qty}",
                "product_materials": product_materials
            })

        # Natija ro'yxati javob sifatida qaytariladi
        return Response({"result": result})
