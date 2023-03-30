from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class NameCapacitiveEquipment(models.Model):  # Основные данные обсчета (название и т.д.)
    name_equipment = models.CharField(max_length=60)  # Наименование "Аппарат емкостной ..."
    type_equipment = models.CharField(max_length=30)  # Тип аппарата (горизонтальный/вертикальный)
    calc_number = models.CharField(max_length=30)  # Номер обсчета (№2055)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )  # Автор
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Fitting(models.Model):  # ШТУЦЕРЫ
    name = models.CharField(max_length=20)  # Название штуцера
    purpose = models.CharField(max_length=60)  # Назначение штуцера
    dn_passage = models.DecimalField(max_digits=8, decimal_places=3)  # Условный проход
    pn = models.DecimalField(max_digits=8, decimal_places=3)  # давление


class BasePipe():
    diameter = models.DecimalField(max_digits=8, decimal_places=3)  # Диаметр
    thickness = models.DecimalField(max_digits=8, decimal_places=3)  # Толщина
    length = models.DecimalField(max_digits=8, decimal_places=3)  # Длинна втулки
    quantity = models.DecimalField(max_digits=6, decimal_places=3)  # Количество


class Bushing(models.Model, BasePipe):  # Модель ВТУЛОК
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)


class BranchPipe(models.Model, BasePipe):  # ПАТРУБКИ
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)


class CaseDevice(models.Model, BasePipe):  # КОРПУС аппарата
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)


class OtherProducts(models.Model):  # ПРОЧИЕ изделия
    name = models.CharField(max_length=60)  # Наименование изделия
    weight = models.DecimalField(max_digits=9, decimal_places=3)  # Масса
    quantity = models.DecimalField(max_digits=6, decimal_places=3)  # Количество
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)
