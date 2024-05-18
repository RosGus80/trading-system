from django.db import models

from users.models import User

# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    email = models.EmailField(**NULLABLE, verbose_name='Почта')
    country = models.CharField(max_length=255, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=255, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=255, **NULLABLE, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Номер дома')

    total_supplier_debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')

    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Factory'
        verbose_name_plural = 'Factories'

    def __str__(self):
        return f'"Factory" object no. {self.pk}, {self.name}'


class Retailer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    email = models.EmailField(**NULLABLE, verbose_name='Почта')
    country = models.CharField(max_length=255, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=255, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=255, **NULLABLE, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Номер дома')

    total_supplier_debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')

    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'

    def __str__(self):
        return f'"Retailer" object no. {self.pk}, {self.name}'


class Entrepreneur(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    email = models.EmailField(**NULLABLE, verbose_name='Почта')
    country = models.CharField(max_length=255, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=255, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=255, **NULLABLE, verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Номер дома')

    total_supplier_debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')

    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Entrepreneur'
        verbose_name_plural = 'Entrepreneurs'

    def __str__(self):
        return f'"Entrepreneur" object no. {self.pk}, {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    version = models.IntegerField(verbose_name='Версия')
    market_access_date = models.DateField(auto_now_add=True, verbose_name='Дата выхода на рынок')

    factory_owner = models.ForeignKey(Factory, **NULLABLE, default=None, on_delete=models.SET_DEFAULT,
                                      verbose_name='Владелец (завод)')
    retailer_owner = models.ForeignKey(Retailer, **NULLABLE, default=None, on_delete=models.SET_DEFAULT,
                                       verbose_name='Владелец (розничная сеть)')
    entrepreneur_owner = models.ForeignKey(Entrepreneur, **NULLABLE, default=None, on_delete=models.SET_DEFAULT,
                                           verbose_name='Владелец (ИП)')

    factory_supplier = models.ForeignKey(Factory, **NULLABLE, default=None, on_delete=models.CASCADE,
                                         verbose_name='Поставщик (завод)', related_name='supplier')
    retailer_supplier = models.ForeignKey(Retailer, **NULLABLE, default=None, on_delete=models.CASCADE,
                                          verbose_name='Поставщик (розничная сеть)', related_name='supplier')
    entrepreneur_supplier = models.ForeignKey(Entrepreneur, **NULLABLE, default=None, on_delete=models.CASCADE,
                                              verbose_name='Поставщик (ИП)', related_name='supplier')

    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'"Product" object no. {self.pk}, {self.name}'

