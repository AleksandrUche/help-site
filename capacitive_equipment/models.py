from django.db import models

'''Инициализация обсчета'''


class NameCapacitiveEquipment(models.Model):
    name = models.CharField(max_length=60)  # Наименование "Аппарат емкостной ..."
    type_equipment = models.CharField(max_length=30)  # Тип аппарата (горизонтальный/вертикальный)
    calc_number = models.CharField(max_length=30)  # Номер обсчета (№2055)
    author =


'''Втулки'''


class Bushing(models.Model):



'''Патрубки'''

'''Корпус'''

'''Прочие изделия'''
class OtherProducts(models.Model):
    name = models.CharField(max_length=60)  # Наименование изделия
    weight = models.DecimalField(max_digits=9, decimal_places=3) # Масса
    quantity = models.DecimalField(max_digits=6, decimal_places=3) # Количество
