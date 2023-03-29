from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

'''Инициализация обсчета'''


class NameCapacitiveEquipment(models.Model):
    name_equipment = models.CharField(max_length=60)  # Наименование "Аппарат емкостной ..."
    type_equipment = models.CharField(max_length=30)  # Тип аппарата (горизонтальный/вертикальный)
    calc_number = models.CharField(max_length=30)  # Номер обсчета (№2055)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)  # Автор
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


# '''Втулки'''
#
#
# class Bushing(models.Model):
#
#
#
# '''Патрубки'''
#
# '''Корпус'''
#
# '''Прочие изделия'''
# class OtherProducts(models.Model):
#     name = models.CharField(max_length=60)  # Наименование изделия
#     weight = models.DecimalField(max_digits=9, decimal_places=3) # Масса
#     quantity = models.DecimalField(max_digits=6, decimal_places=3) # Количество
