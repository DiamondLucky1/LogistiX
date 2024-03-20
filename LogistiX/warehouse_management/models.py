
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


#Модель склада
class Warehouse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название склада')
    location = models.CharField(max_length=100, verbose_name='Расположение')
    capacity = models.IntegerField(verbose_name='Объем')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категория товара')

    class Meta:
        verbose_name = 'Категори'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name



#хранение информации о конкретных товарах, которые находятся на складе
class InventoryItem(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='На каком складе находится')
    name = models.CharField(max_length=100, verbose_name='Название товара')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество единиц товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара', blank=True)
    characteristic = models.TextField(blank=True, verbose_name='Характеристика')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица инвентаря'
        verbose_name_plural = 'Единицы инвентаря'


#регистрации производственных операций
class Production(models.Model):
    product = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, verbose_name='Название производства')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    date_produced = models.DateTimeField(default=timezone.now, verbose_name='Дата производства')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


#отслеживания перемещения товаров между различными складскими местами
class StockMovement(models.Model):
    product = models.ForeignKey('InventoryItem', on_delete=models.CASCADE, verbose_name='Инвентарь')#позволяет связать движение товара со соответствующим товаром в инвентаре.
    quantity = models.IntegerField(verbose_name='количество товаров')#количество товаров, которые были перемещены
    source_location = models.ForeignKey('Warehouse', related_name='source_location', on_delete=models.CASCADE)#склад, с которого были перемещены товары
    destination_location = models.ForeignKey('Warehouse', related_name='destination_location', on_delete=models.CASCADE)#склад, на который они были перемещены
    date_moved = models.DateTimeField(default=timezone.now)#время проведения перемещения товаров
    moved_by = models.ForeignKey(User, on_delete=models.CASCADE)#пользователь, который провел перемещение товаров


