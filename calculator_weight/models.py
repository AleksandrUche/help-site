from django.db import models


class CornerEqualShelvesGost(models.Model):
    name = models.CharField(verbose_name='Размер', max_length=10)
    side = models.DecimalField(verbose_name='Сторона уголка, a', max_digits=5, decimal_places=1)
    thickness = models.DecimalField(verbose_name='Толщина, t', max_digits=5, decimal_places=1)
    weight = models.FloatField(verbose_name='Масса, 1м/кг')
