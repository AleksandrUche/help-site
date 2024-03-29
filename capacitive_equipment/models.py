from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class TypeEquipment(models.Model):
    """Тип оборудования(аппарат горизонтальный/вертикальный и т.д.)"""
    name = models.CharField('Тип аппарата', max_length=30, help_text='горизонтальный/вертикальный')

    class Meta:
        verbose_name = 'тип емкостного аппарата'
        verbose_name_plural = 'Тип оборудования'

    def __str__(self):
        return self.name


class Material(models.Model):
    """Плотность металлов"""
    name = models.CharField('Наименование металла', max_length=30)
    density = models.DecimalField('Плотность металла (кг/м3)', max_digits=6, decimal_places=3)

    def __str__(self):
        return self.name


"""_____ОСНОВНЫЕ ПАРАМЕТРЫ ОБСЧЕТА_____"""


class NameCapacitiveEquipment(models.Model):  # Основные данные обсчета (название и т.д.)
    """Модель для инициализации обсчетов"""
    name_equipment = models.CharField('Наименование аппарата', max_length=60)  # Наименование "Аппарат емкостной ..."
    type_equipment = models.ForeignKey(
        TypeEquipment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип аппарата',
    )  # Тип аппарата (горизонтальный/вертикальный)
    calc_number = models.CharField('Наряд-заказ №', max_length=30, unique=True)  # Номер обсчета (№2055)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Автор обсчета',
    )  # Автор
    created_date = models.DateTimeField('Дата создания', default=timezone.now)  # дата добавления

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'обсчеты'
        verbose_name_plural = 'Обсчет (наименование)'

    def __str__(self):
        return self.calc_number

    def get_absolute_url(self):
        return reverse('detail_name_calc_capac', kwargs={'pk': self.pk})


class Parameter(models.Model):
    """Параметры аппарата"""
    SUPPORT_CAPACITIVE_DEVICE_CHOICES = [
        ('ОСТ 26-2091-93', 'Горизонтальные ОСТ 26-2091-93'),
        ('АТК 24.200.03-90', 'Вертикальные АТК 24.200.03-90')
    ]
    calculation_object = models.OneToOneField(
        NameCapacitiveEquipment,
        related_name='parameters',
        on_delete=models.CASCADE,
    )
    support_capacitive_device = models.CharField(
        max_length=40,
        choices=SUPPORT_CAPACITIVE_DEVICE_CHOICES,
        verbose_name='Тип опор',
    )
    support_capacitive_device_quantity = models.IntegerField('Количество опор')
    thermal_insulation = models.CharField('Наличие теплоизоляции', max_length=200)  # Возможно добавление выбора!
    thermal_insulation_quantity = models.IntegerField('Количество крепления для теплоизоляции')
    thermal_insulation_type = models.CharField(
        max_length=10, choices=[('С2', 'Скоба С2'), ('В1', 'Втулка В1')],
        verbose_name='Тип крепления для теплоизоляции',
    )
    overlays_service_platform = models.CharField(
        max_length=10, choices=[('Да', 'Да'), ('Нет', 'Нет')],
        verbose_name='Накладки для площадки',
    )
    ladder = models.CharField(
        max_length=10,
        choices=[('Нет', 'Нет'), ('Да, 1 шт.', 'Да, 1 шт.'), ('Да, 2 шт.', 'Да, 2 шт.')],
        verbose_name='Лестница внутри аппарата',
    )
    hydrogen_sulfide = models.CharField(
        max_length=5,
        choices=[('Да', 'Да'), ('Нет', 'Нет')],
        verbose_name='Содержание сероводорода',
    )
    hydrogen_sulfide_group = models.CharField(
        'Группа по ГОСТ 34233.1-2017',
        max_length=5,
        blank=True,
        null=True,
    )
    corrosion = models.IntegerField('Коррозия, мм')
    service_life = models.IntegerField('Срок службы, лет')
    heat_treatment = models.CharField(
        max_length=5,
        choices=[('Да', 'Да'), ('Нет', 'Нет')],
        verbose_name='Термообработка',
    )
    working_temperature = models.CharField('Температура рабочая', max_length=40)
    calculated_temperature = models.CharField('Температура расчетная', max_length=10)
    design_pressure = models.CharField('Расчетное давление', max_length=10)
    density = models.CharField('Плотность рабочей среды', max_length=50)
    steaming_temperature = models.CharField('Температура пропарки', max_length=100)
    seismic_activity = models.CharField('Сейсмичность, баллов', max_length=5)
    coating_external = models.CharField('Наружное покрытие', max_length=200)
    coating_internal = models.CharField('Внутренне покрытие', max_length=200)
    conservation_requirement = models.CharField('Требование консервации', max_length=150)
    visual_identification = models.CharField('Требования к визуальной идентификации', max_length=200)
    spare_parts = models.CharField('ЗИП', max_length=200)
    departures_fittings = models.CharField('Вылеты штуцеров', max_length=250)
    flange_coils = models.CharField(
        max_length=5,
        choices=[('Да', 'Да'), ('Нет', 'Нет')],
        verbose_name='Наличие фланцевых катушек',
    )
    rotary_fl_stoppers = models.CharField(
        max_length=5,
        choices=[('Да', 'Да'), ('Нет', 'Нет')],
        verbose_name='Наличие поворотных заглушек',
    )

    class Meta:
        verbose_name = 'параметры обсчета'
        verbose_name_plural = 'Параметры обсчета'

    def __str__(self):
        return self.calculation_object

    def get_absolute_url(self):
        return reverse('detail_parameter_calc_capac', kwargs={'slug': self.pk})


"""_____МОДЕЛИ ДЛЯ ОБСЧЕТА МАСС_____"""


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
    calculation_object = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)
    material = models.ForeignKey(
        Material,
        on_delete=models.SET_DEFAULT,
        null=True,
        default='не указан',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.diameter, self.thickness


class Bushing(BasePipe):  # ВТУЛКИ
    """Модель для втулок"""


class BranchPipe(BasePipe):  # ПАТРУБКИ
    """Модель для труб"""


class CaseDevice(BasePipe):  # КОРПУС аппарата
    """Корпус аппарата"""


class Bottoms(models.Model):
    """Днища, которые входят в обсчет"""

    calculation = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)


class OtherProducts(models.Model):  # ПРОЧИЕ изделия
    """Прочие изделия, например скобы для теплоизоляции и т.д"""
    name = models.CharField('Наименование изделия', max_length=60)  # Наименование изделия
    weight = models.DecimalField('Масса', max_digits=9, decimal_places=3)  # Масса
    quantity = models.DecimalField('Количество', max_digits=6, decimal_places=3)  # Количество
    calculation_id = models.ForeignKey(NameCapacitiveEquipment, on_delete=models.CASCADE)
