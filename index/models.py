from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoodType(models.Model):
    """定义商品类别"""
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Good(models.Model):
    """这是商品管理的模型"""
    goods_type = models.ForeignKey(GoodType)
    goods_name = models.CharField(max_length=15)
    last_price = models.FloatField()
    add_people = models.ForeignKey(User)
    update_time = models.DateTimeField(auto_now_add=True)
    recent_sell = models.DateField(blank=True, null=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        """返回物品名称"""
        return self.goods_name


class Order(models.Model):
    """定义订单模型"""
    name = models.CharField(max_length=20)
    customer = models.CharField(max_length=10, default='无')
    phonenumber = models.CharField(max_length=13, default='无')
    address = models.CharField(max_length=50, default='无')
    goods = models.TextField(blank=True, null=True)
    total_prices = models.FloatField(default=0)
    total_profit = models.FloatField(default=0)
    is_delete = models.BooleanField(default=False)
    c_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    """定义门店类型"""
    name = models.CharField(max_length=15)
    boss = models.ForeignKey(User)  # 老板

    def __str__(self):
        """显示子门店名称"""
        return self.name


class GoodsShop(models.Model):
    """子门店"""
    goods = models.ForeignKey(Good)
    shop = models.ForeignKey(Shop)
    last_updater = models.ForeignKey(User)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s--%s" % (self.shop, self.goods)

class Inventory(models.Model):
    """定义货物清单"""
    goods = models.ForeignKey(Good)
    shop = models.ForeignKey(Shop)
    change_num = models.IntegerField()
    updater = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s--%s" % (self.shop, self.goods)

class GoodsSellRecord(models.Model):
    """商品销售记录"""
    goods = models.ForeignKey(Good)
    shop = models.ForeignKey(Shop)
    sell_num = models.IntegerField()
    origin_price = models.FloatField()
    sell_price = models.FloatField()
    customer = models.CharField(max_length=10, default='无')
    phonenumber = models.CharField(max_length=13, default='无')
    address = models.CharField(max_length=50, default='无')
    order = models.ForeignKey(Order, blank=True, null=True)
    is_delete = models.BooleanField(default=False)
    updater = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def get_profit(self):
        profit = (self.sell_price-self.origin_price) * self.sell_num
        return profit

    def get_receivable(self):
        receivable = self.sell_num * self.sell_price
        return receivable

    def __str__(self):
        return u"%s--%s" % (self.shop, self.goods)



class GoodsAddRecord(models.Model):
    """库存增加记录"""
    goods = models.ForeignKey(Good)
    shop = models.ForeignKey(Shop)
    num = models.IntegerField()
    price = models.FloatField()
    updater = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s--%s" % (self.shop, self.goods)
