from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TypeEquipment(models.Model):
    """Тип оборудования(аппарат горизонтальный/вертикальный и т.д.)"""
    name = models.CharField('Тип аппарата', max_length=30)


class NameCapacitiveEquipment(models.Model):  # Основные данные обсчета (название и т.д.)
    """Модель для инициализации обсчетов"""
    name_equipment = models.CharField('Наименование аппарата', max_length=60)  # Наименование "Аппарат емкостной ..."
    type_equipment = models.ForeignKey(TypeEquipment,
                                       on_delete=models.SET_NULL,
                                       null=True)  # Тип аппарата (горизонтальный/вертикальный)
    calc_number = models.CharField('Наряд-заказ', max_length=30)  # Номер обсчета (№2055)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               null=True,
                               default='пользователь удален')  # Автор
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.calc_number


class Fitting(models.Model):  # ШТУЦЕРЫ
    """Модель для штуцеров"""
    name = models.CharField('Название штуцера', max_length=20)  # Название штуцера
    purpose = models.CharField('Назначение штуцера', max_length=60)  # Назначение штуцера
    dn_passage = models.DecimalField('Условный проход', max_digits=8, decimal_places=3)  # Условный проход
    pn = models.DecimalField('Давление номинальное', max_digits=8, decimal_places=3)  # давление

    def __str__(self):
        return self.name


class BasePipe(models.Model):
    """Базовая модель для патрубков/втулок/обечаек"""
    diameter = models.DecimalField('Диаметр', max_digits=8, decimal_places=3)  # Диаметр
    thickness = models.DecimalField('Толщина', max_digits=8, decimal_places=3)  # Толщина
    length = models.DecimalField('Длинна', max_digits=8, decimal_places=3)  # Длинна втулки
    quantity = models.DecimalField('Количество', max_digits=6, decimal_places=3)  # Количество
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.diameter, self.thickness

    class Meta:
        abstract = True


class Bushing(BasePipe):  # ВТУЛКИ
    """Модель для втулок"""


class BranchPipe(BasePipe):  # ПАТРУБКИ
    """Модель для труб"""


class CaseDevice(BasePipe):  # КОРПУС аппарата
    """Корпус аппарата"""


class Bottoms(models.Model):
    """Днища, которые входят в обсчет"""
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)


class OtherProducts(models.Model):  # ПРОЧИЕ изделия
    """Прочие изделия, например"""
    name = models.CharField('Наименование изделия', max_length=60)  # Наименование изделия
    weight = models.DecimalField('Масса', max_digits=9, decimal_places=3)  # Масса
    quantity = models.DecimalField('Количество', max_digits=6, decimal_places=3)  # Количество
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)
