# product_count

Ushbu app orqali ombordagi xomashyolarni nazorat qilish uchun qulay imkoniyatga ega bo'lasiz. 

Ishlash ketma ketligini sanab o'tamiz:                                                                      URLS 
1. Mahsulot qo'shish                                                                                        /product/
2. Xom-ashyo qo'shish                                                                                       /product/material/
3. Xomashyoning miqdor birligini qo'shish                                                                   /product/unity/
4. Bir dona mahsulot uchun qanday xomashyo ishlatilishi va xomashyoning miqdorini kiritish                  /product/one/pro/material/
5. Omborga Xom-ashyo partiyasi va uning miqdori va bir miqdordagi xomashyo uchun narini qo'shish            /warehouse/material/

Malumot olish
1. Kerakli mahsulotni tanlash va uning miqdorini kiritish kifoya.                                           /info/
    Postman orqali request yuborganda quydagi tartibda POST request yuborish kifoya

    {"product_list":[
        {
            "product_name": 1,
            "product_qty": 20
        },
        {
            "product_name": 2,
            "product_qty": 30
        },
        ...
        ...
        ...
    ]}


Ishlatilgan texnologiyalar
1. Django==5.0.3
2. djangorestframework==3.14.0
3. sqlite3
