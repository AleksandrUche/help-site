from django.db import models


class CornerEqualShelvesGost(models.Model):
    """Модель для уголков равнополочных"""
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

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ChannelTypeY(SteelChannelBase):
    """Швеллер тип У"""
    class Meta:
        verbose_name = 'швеллеры серии "У"'
        verbose_name_plural = 'Швеллер "У" ГОСТ 8240-97'


class ChannelTypeP(SteelChannelBase):
    """Швеллер тип П"""
    class Meta:
        verbose_name = 'швеллеры серии "П"'
        verbose_name_plural = 'Швеллер "П" ГОСТ 8240-97'


class ChannelTypeE(SteelChannelBase):
    """Швеллер тип Э"""
    class Meta:
        verbose_name = 'швеллеры серии "Э"'
        verbose_name_plural = 'Швеллер "Э" ГОСТ 8240-97'


class ChannelTypeL(SteelChannelBase):
    """Швеллер тип Л"""
    class Meta:
        verbose_name = 'швеллеры серии "Л"'
        verbose_name_plural = 'Швеллер "Л" ГОСТ8240-97'


class ChannelTypeC(SteelChannelBase):
    """Швеллер тип С"""
    class Meta:
        verbose_name = 'швеллеры серии "С"'
        verbose_name_plural = 'Швеллер "С" ГОСТ8240-97'


"""Двутавры"""


class BeamGost8239(SteelChannelBase):
    """Двутавр по ГОСТ 8239-89"""
    class Meta:
        verbose_name = 'двутавры по ГОСТ 8239-89'
        verbose_name_plural = 'Двутавры ГОСТ 8239-89'


class BeamGost26020TypeB(SteelChannelBase):
    """Двутавр тип Б"""
    class Meta:
        verbose_name = 'двутавры тип "Б" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Б"'


class BeamGost26020TypeSh(SteelChannelBase):
    """Двутавр тип Ш"""
    class Meta:
        verbose_name = 'двутавры тип "Ш" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Ш"'


class BeamGost26020TypeK(SteelChannelBase):
    """Двутавр тип К"""
    class Meta:
        verbose_name = 'двутавры тип "К" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "К"'


class BeamGost26020TypeD(SteelChannelBase):
    """Двутавр тип Д"""
    class Meta:
        verbose_name = 'двутавры тип "Д" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "Д"'


class BeamGost26020TypeS(SteelChannelBase):
    """Двутавр тип С"""
    class Meta:
        verbose_name = 'двутавры тип "С" по ГОСТ 26020-83'
        verbose_name_plural = 'Двутавры ГОСТ 26020-83 тип "С"'
