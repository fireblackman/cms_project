from django.contrib import admin
from .models import Good,Shop,Order,Inventory,GoodsAddRecord,GoodsSellRecord,GoodsShop,GoodType
# Register your models here.

admin.site.register(Good)
admin.site.register(Shop)
admin.site.register(Inventory)
admin.site.register(GoodsShop)
admin.site.register(GoodsSellRecord)
admin.site.register(GoodsAddRecord)
admin.site.register(Order)
admin.site.register(GoodType)