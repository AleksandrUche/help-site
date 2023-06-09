from django.db import models


class CornerEqualShelvesGost(models.Model):
    name = models.CharField(verbose_name='Размер', max_length=10)
    side = models.FloatField(verbose_name='Сторона уголка, a')
    thickness = models.FloatField(verbose_name='Толщина, t')
    weight = models.FloatField(verbose_name='Масса, 1м/кг')


class SteelChannelBase(models.Model):
    """Базовая модель швеллеров"""
    name = models.CharField(verbose_name='Номер швеллера', max_length=10)
    height = models.FloatField(verbose_name='h')
    width = models.FloatField(verbose_name='b')
    thickness = models.FloatField(verbose_name='s')
    thickness_t = models.FloatField(verbose_name='t')
    weight = models.FloatField(verbose_name='Масса, 1м/кг')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ChannelTypeY(SteelChannelBase):
    class Meta:
        verbose_name = 'швеллеры серии "У"'
        verbose_name_plural = 'Швеллер "У" ГОСТ 8240-97'


class ChannelTypeP(SteelChannelBase):
    class Meta:
        verbose_name = 'швеллеры серии "П"'
        verbose_name_plural = 'Швеллер "П" ГОСТ 8240-97'


class ChannelTypeE(SteelChannelBase):
    class Meta:
        verbose_name = 'швеллеры серии "Э"'
        verbose_name_plural = 'Швеллер "Э" ГОСТ 8240-97'


class ChannelTypeL(SteelChannelBase):
    class Meta:
        verbose_name = 'швеллеры серии "Л"'
        verbose_name_plural = 'Швеллер "Л" ГОСТ8240-97'


class ChannelTypeC(SteelChannelBase):
    class Meta:
        verbose_name = 'швеллеры серии "С"'
        verbose_name_plural = 'Швеллер "С" ГОСТ8240-97'


"""Двутавры"""


class BeamGost8239(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры по ГОСТ 8239-89'
        verbose_name_plural = 'Двутавры ГОСТ 8239-89'


class BeamGost26020TypeB(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры тип "Б" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Б"'


class BeamGost26020TypeSh(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры тип "Ш" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Ш"'


class BeamGost26020TypeK(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры тип "К" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "К"'


class BeamGost26020TypeD(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры тип "Д" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Д"'


class BeamGost26020TypeS(SteelChannelBase):
    class Meta:
        verbose_name = 'двутавры тип "С" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "С"'
