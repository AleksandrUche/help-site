from django.db import models


class Documents(models.Model):
    """Динамическое меню стандартов"""
    title = models.CharField(max_length=30)
    url = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name="URL")
    description = models.CharField(max_length=200)
    cat_id = models.ForeignKey('CategoryDoc', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title


class CategoryDoc(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Gost33259AvailabilityFlange(models.Model):
    """Наличие фланца в ГОСТ 33259-2015"""
    pn = models.CharField(max_length=6, verbose_name='PN')
    type_fl = models.CharField(max_length=6, verbose_name='Тип фланца')
    dn_10 = models.BooleanField(default=False)
    dn_15 = models.BooleanField(default=False)
    dn_20 = models.BooleanField(default=False)
    dn_25 = models.BooleanField(default=False)
    dn_32 = models.BooleanField(default=False)
    dn_40 = models.BooleanField(default=False)
    dn_50 = models.BooleanField(default=False)
    dn_65 = models.BooleanField(default=False)
    dn_80 = models.BooleanField(default=False)
    dn_100 = models.BooleanField(default=False)
    dn_125 = models.BooleanField(default=False)
    dn_150 = models.BooleanField(default=False)
    dn_200 = models.BooleanField(default=False)
    dn_250 = models.BooleanField(default=False)
    dn_300 = models.BooleanField(default=False)
    dn_350 = models.BooleanField(default=False)
    dn_400 = models.BooleanField(default=False)
    dn_450 = models.BooleanField(default=False)
    dn_500 = models.BooleanField(default=False)
    dn_600 = models.BooleanField(default=False)
    dn_700 = models.BooleanField(default=False)
    dn_800 = models.BooleanField(default=False)
    dn_900 = models.BooleanField(default=False)
    dn_1000 = models.BooleanField(default=False)
    dn_1200 = models.BooleanField(default=False)
    dn_1400 = models.BooleanField(default=False)
    dn_1600 = models.BooleanField(default=False)
    dn_1800 = models.BooleanField(default=False)
    dn_2000 = models.BooleanField(default=False)
    dn_2200 = models.BooleanField(default=False)
    dn_2400 = models.BooleanField(default=False)
    dn_2600 = models.BooleanField(default=False)
    dn_2800 = models.BooleanField(default=False)
    dn_3000 = models.BooleanField(default=False)
    dn_3200 = models.BooleanField(default=False)
    dn_3400 = models.BooleanField(default=False)
    dn_3600 = models.BooleanField(default=False)
    dn_4000 = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'наличе фланцев ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 наличе фланцев '
        ordering = ['id']

    def __str__(self):
        return self.pn


class Gost33259Type01(models.Model):
    """Размеры фланцев ГОСТ 33259-2015 ТИП 01"""
    dn_passage = models.IntegerField(verbose_name='DN')
    pn = models.FloatField(verbose_name='PN')
    dv_lower_row_one = models.CharField(blank=True, max_length=20, verbose_name='dв')  # ряд 1
    dv_lower_row_two = models.CharField(blank=True, max_length=20, verbose_name='dв')  # ряд 2
    b_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 1
    b_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 2
    c1_lower = models.CharField(blank=True, max_length=6, verbose_name='c1')
    d_row_one = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 1
    d_row_two = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 2
    d1 = models.CharField(blank=True, max_length=6, verbose_name='D1')
    d_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 1
    d_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 2
    n_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 1
    n_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 2
    pin_row_one = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 1
    pin_row_two = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 2

    class Meta:
        verbose_name = 'тип 01 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 01'
        ordering = ['id']

    def __str__(self):
        return self.dn_passage


class Gost33259Type02(models.Model):
    """Размеры фланцев ГОСТ 33259-2015 ТИП 02"""
    dn_passage = models.IntegerField(verbose_name='DN')
    pn = models.FloatField(verbose_name='PN')
    d0_row_one = models.CharField(blank=True, max_length=20, verbose_name='D0')  # ряд 1
    d0_row_two = models.CharField(blank=True, max_length=20, verbose_name='D0')  # ряд 2
    d2 = models.CharField(blank=True, max_length=6, verbose_name='D2')
    dv_lower_row_one = models.CharField(blank=True, max_length=20, verbose_name='dв')  # ряд 1
    dv_lower_row_two = models.CharField(blank=True, max_length=20, verbose_name='dв')  # ряд 2
    b_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 1
    b_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 2
    b1_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='b1')  # ряд 1
    b1_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='b1')  # ряд 2
    c_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='c')  # ряд 1
    c_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='c')  # ряд 2
    c1_lower = models.CharField(blank=True, max_length=6, verbose_name='c1')
    d_row_one = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 1
    d_row_two = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 2
    d1 = models.CharField(blank=True, max_length=6, verbose_name='D1')
    d_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 1
    d_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 2
    n_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 1
    n_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 2
    pin_row_one = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 1
    pin_row_two = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 2

    class Meta:
        verbose_name = 'тип 02 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 02 '
        ordering = ['id']

    def __str__(self):
        return self.dn_passage


class Gost33259Type11(models.Model):
    """Размеры фланцев ГОСТ 33259-2015 ТИП 11"""
    dn_passage = models.IntegerField(verbose_name='DN')
    pn = models.FloatField(verbose_name='PN')
    dm_row_one = models.CharField(blank=True, max_length=6, verbose_name='Dm')  # ряд 1
    dm_row_two = models.CharField(blank=True, max_length=6, verbose_name='Dm')  # ряд 2
    dn_row_one = models.CharField(blank=True, max_length=6, verbose_name='Dn')  # ряд 1
    dn_row_two = models.CharField(blank=True, max_length=6, verbose_name='Dn')  # ряд 2
    d1_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='d1')  # ряд 1
    d1_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='d1')  # ряд 2
    b_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 1
    b_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='b')  # ряд 2
    h_row_one = models.CharField(blank=True, max_length=6, verbose_name='H')  # ряд 1
    h_row_two = models.CharField(blank=True, max_length=6, verbose_name='H')  # ряд 2
    h1 = models.CharField(blank=True, max_length=6, verbose_name='H1')
    d_row_one = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 1
    d_row_two = models.CharField(blank=True, max_length=6, verbose_name='D')  # ряд 2
    d1 = models.CharField(blank=True, max_length=6, verbose_name='D1')
    d_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 1
    d_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='d')  # ряд 2
    n_lower_row_one = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 1
    n_lower_row_two = models.CharField(blank=True, max_length=6, verbose_name='n')  # ряд 2
    pin_row_one = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 1
    pin_row_two = models.CharField(blank=True, max_length=6, verbose_name='Диаметр шпилек')  # ряд 2

    class Meta:
        verbose_name = 'тип 11 ГОСТ 33259-2015'
        verbose_name_plural = 'ГОСТ 33259-2015 тип 11'
        ordering = ['id']

    def __str__(self):
        return self.dn_passage


class Gost33259SurfaceValues(models.Model):  #
    """Уплотнительные поверхности для всех фланцев ГОСТ 33259-2015"""
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.FloatField(verbose_name='PN')
    d2 = models.CharField(blank=True, max_length=6, verbose_name='D2')
    d3_row_one = models.CharField(blank=True, max_length=6, verbose_name='D3')  # ряд 1
    d3_row_two = models.CharField(blank=True, max_length=6, verbose_name='D3')  # ряд 2
    d4_row_one = models.CharField(blank=True, max_length=6, verbose_name='D4')  # ряд 1
    d4_row_two = models.CharField(blank=True, max_length=6, verbose_name='D4')  # ряд 2
    d5_row_one = models.CharField(blank=True, max_length=6, verbose_name='D5')  # ряд 1
    d5_row_two = models.CharField(blank=True, max_length=6, verbose_name='D5')  # ряд 2
    d6_row_one = models.CharField(blank=True, max_length=6, verbose_name='D6')  # ряд 1
    d6_row_two = models.CharField(blank=True, max_length=6, verbose_name='D6')  # ряд 2
    d7 = models.CharField(blank=True, max_length=6, verbose_name='D7')
    d8 = models.CharField(blank=True, max_length=6, verbose_name='D8')
    d9 = models.CharField(blank=True, max_length=6, verbose_name='D9')
    d10 = models.CharField(blank=True, max_length=6, verbose_name='D10')
    d11 = models.CharField(blank=True, max_length=6, verbose_name='D11')
    b2_lower = models.CharField(blank=True, max_length=6, verbose_name='b2')
    h_lower = models.CharField(blank=True, max_length=6, verbose_name='h')
    h1_lower = models.CharField(blank=True, max_length=6, verbose_name='h1')
    h2_lower = models.CharField(blank=True, max_length=6, verbose_name='h2')
    h3_lower = models.CharField(blank=True, max_length=6, verbose_name='h3')
    h4_lower = models.CharField(blank=True, max_length=6, verbose_name='h4')
    h5_lower = models.CharField(blank=True, max_length=6, verbose_name='h5')

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'ГОСТ 33259-2015 уплотнительная поверхность '
        ordering = ['id']

    def __str__(self):
        return self.dn_passage


class Gost33259Mass(models.Model):
    """Масса фланцев ГОСТ 33259-2015"""
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    type_fl = models.CharField(max_length=6, verbose_name='Тип')
    pn_1 = models.CharField(max_length=6, verbose_name='PN 1')
    pn_2 = models.CharField(max_length=6, verbose_name='PN 2,5')
    pn_6 = models.CharField(max_length=6, verbose_name='PN 6')
    pn_10 = models.CharField(max_length=6, verbose_name='PN 10')
    pn_16 = models.CharField(max_length=6, verbose_name='PN 16')
    pn_25 = models.CharField(max_length=6, verbose_name='PN 25')
    pn_40 = models.CharField(max_length=6, verbose_name='PN 40')
    pn_63 = models.CharField(max_length=6, verbose_name='PN 63')
    pn_100 = models.CharField(max_length=6, verbose_name='PN 100')
    pn_160 = models.CharField(max_length=6, verbose_name='PN 160')
    pn_200 = models.CharField(max_length=6, verbose_name='PN 200')

    class Meta:
        verbose_name = 'массы'
        verbose_name_plural = 'ГОСТ 33259-2015 массы'
        ordering = ['id']

    def __str__(self):
        return self.dn_passage


class Gost33259TypeDrawing(models.Model):
    """Чертеж "типа" фланца ГОСТ 33259-2015"""
    type_fl = models.CharField(max_length=6, verbose_name='Тип фланца')
    flange_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'типы'
        verbose_name_plural = 'ГОСТ 33259-2015 чертежи типов фланцев'

    def __str__(self):
        return self.type_fl


class Gost33259SurfaceDrawing(models.Model):
    """Чертеж уплотнительной поверхности фланца ГОСТ 33259-2015"""
    surface_fl = models.CharField(max_length=6, verbose_name='Уплотнительная поверхность')
    surface_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'уплотнительные поверхности'
        verbose_name_plural = 'ГОСТ 33259-2015 чертежи уплотнительной поверхность'

    def __str__(self):
        return self.surface_fl


class Atk261813FlangeExec1(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 1"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 1'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 1'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeExec2(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 2"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 2'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 2'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeExec3(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 3"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d6 = models.CharField(max_length=6, verbose_name='D6')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 3'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 3'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeExec4(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 4"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 4'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 4'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeExec5(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 5"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d5 = models.CharField(max_length=6, verbose_name='D5')
    d6 = models.CharField(max_length=6, verbose_name='D6')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 5'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 5'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeExec6(models.Model):
    """Фланцы АТК 26-18-13-96 Исполнение 6"""
    dn_passage = models.CharField(max_length=6, verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d8 = models.CharField(max_length=6, verbose_name='D8')
    d9 = models.CharField(max_length=6, verbose_name='D9')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h3_lower = models.CharField(max_length=6, verbose_name='h3')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    dm = models.CharField(max_length=6, verbose_name='Dm')
    dn = models.CharField(max_length=6, verbose_name='Dn')
    r_lower = models.CharField(max_length=6, verbose_name='r')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    m = models.CharField(max_length=6, verbose_name='Масса')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')

    class Meta:
        verbose_name = 'исполнение 6'
        verbose_name_plural = 'АТК 26-18-13-96 исполнение 6'

    def __str__(self):
        return self.dn_passage


class Atk261813FlangeDrawing(models.Model):
    """Чертежи фланцев АТК 26-18-13-96"""
    execution_fl = models.CharField(max_length=6, verbose_name='Исполнение фланца')
    execution_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'чертежи фланца'
        verbose_name_plural = 'АТК 26-18-13-96 чертежи исполнений'

    def __str__(self):
        return self.execution_fl


class Gost28759FlangeValues(models.Model):
    """Основные размеры фланцев ГОСТ 28759.3-2022 """
    dn_passage = models.IntegerField(verbose_name='DN')
    pn = models.FloatField(verbose_name='PN')
    d1 = models.CharField(blank=True, max_length=6, verbose_name='D1')
    d2 = models.CharField(blank=True, max_length=6, verbose_name='D2')
    d3 = models.CharField(blank=True, max_length=6, verbose_name='D3')
    d4 = models.CharField(blank=True, max_length=6, verbose_name='D4')
    a_lower = models.CharField(blank=True, max_length=6, verbose_name='a')
    d5 = models.CharField(blank=True, max_length=6, verbose_name='D5')
    a1_lower = models.CharField(blank=True, max_length=6, verbose_name='a1')
    s = models.CharField(blank=True, max_length=6, verbose_name='S0')
    d6 = models.CharField(blank=True, max_length=6, verbose_name='D6')
    d7 = models.CharField(blank=True, max_length=6, verbose_name='D7')
    b_lower = models.CharField(blank=True, max_length=6, verbose_name='b')
    h = models.CharField(blank=True, max_length=6, verbose_name='H')
    d_lower = models.CharField(blank=True, max_length=6, verbose_name='d')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    quantity_pin = models.CharField(max_length=6, verbose_name='Количество шпилек')

    class Meta:
        verbose_name = 'размеры фланцев'
        verbose_name_plural = 'ГОСТ 28759.3-2022 размеры фланцев'

    def __str__(self):
        return self.dn_passage


class Gost28759FlangeMass(models.Model):
    """Массы фланцев ГОСТ 28759.3-2022 """
    dn_passage = models.CharField(max_length=6, verbose_name='DN')
    pn = models.CharField(max_length=6, verbose_name='PN')
    exec_1 = models.FloatField(verbose_name='PN 1')
    exec_2 = models.FloatField(verbose_name='PN 2')
    exec_3 = models.FloatField(verbose_name='PN 3')
    exec_4 = models.FloatField(verbose_name='PN 4')
    exec_5 = models.FloatField(verbose_name='PN 5')
    exec_6 = models.FloatField(verbose_name='PN 6')
    exec_7 = models.FloatField(verbose_name='PN 7')
    exec_8 = models.FloatField(verbose_name='PN 8')

    class Meta:
        verbose_name = 'массы фланцев'
        verbose_name_plural = 'ГОСТ 28759.3-2022 Массы'

    def __str__(self):
        return self.dn_passage


class Gost28759FlangeDrawing(models.Model):
    """Чертежи фланцев ГОСТ 28759.3-2022 """
    execution_fl = models.CharField(max_length=6, verbose_name='Исполнение фланца')
    execution_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'чертежи фланца'
        verbose_name_plural = 'ГОСТ 28759.3-2022 чертежи исполнений'

    def __str__(self):
        return self.execution_fl


class Gost6533Bottoms(models.Model):
    """Основные размеры для днищ ГОСТ 6533-78"""
    exec = models.CharField(max_length=6, verbose_name='Чертеж')
    d = models.IntegerField(verbose_name='D')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    hn_lower = models.CharField(max_length=6, verbose_name='h')
    s_lower = models.CharField(max_length=6, verbose_name='s')
    m = models.CharField(max_length=10, verbose_name='Масса')

    class Meta:
        verbose_name = 'размеры днищ'
        verbose_name_plural = 'Днища ГОСТ 6533-78 размеры'

    def __str__(self):
        return self.d


class Gost6533BottomsDrawing(models.Model):
    """Чертежи для днищ ГОСТ 6533-78"""
    execution = models.CharField(max_length=6, verbose_name='Чертеж')
    execution_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж днища')

    class Meta:
        verbose_name = 'чертежи днищ'
        verbose_name_plural = 'Днища ГОСТ 6533-78 чертежи исполнений'

    def __str__(self):
        return self.execution


class Atk24200FlangeStoppersExec1(models.Model):
    """Размеры "Исполнения 1" для заглушек АТК 24.200.02-90"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d2_lowe = models.CharField(max_length=6, verbose_name='d2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 1'
        verbose_name_plural = 'АТК 24.200.02-90 исполнение 1'

    def __str__(self):
        return self.dn_passage


class Atk24200FlangeStoppersExec2(models.Model):
    """Размеры "Исполнения 2" для заглушек АТК 24.200.02-90"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d2_lowe = models.CharField(max_length=6, verbose_name='d2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 2'
        verbose_name_plural = 'АТК 24.200.02-90 исполнение 2'

    def __str__(self):
        return self.dn_passage


class Atk24200FlangeStoppersExec3(models.Model):
    """Размеры "Исполнения 3" для заглушек АТК 24.200.02-90"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d3 = models.CharField(max_length=6, verbose_name='D3')
    d4 = models.CharField(max_length=6, verbose_name='D4')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d2_lowe = models.CharField(max_length=6, verbose_name='d2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 3'
        verbose_name_plural = 'АТК 24.200.02-90 исполнение 3'

    def __str__(self):
        return self.dn_passage


class Atk24200FlangeStoppersExec4(models.Model):
    """Размеры "Исполнения 4" для заглушек АТК 24.200.02-90"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d8 = models.CharField(max_length=6, verbose_name='D8')
    b2_lower = models.CharField(max_length=6, verbose_name='b2')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    r_lower = models.CharField(max_length=6, verbose_name='r')
    d2_lowe = models.CharField(max_length=6, verbose_name='d2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 4'
        verbose_name_plural = 'АТК 24.200.02-90 исполнение 4'

    def __str__(self):
        return self.dn_passage


class Atk24200FlangeStoppersExec5(models.Model):
    """Размеры "Исполнения 5" для заглушек АТК 24.200.02-90"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d6 = models.CharField(max_length=6, verbose_name='D6')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d2_lowe = models.CharField(max_length=6, verbose_name='d2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    n_lower = models.CharField(max_length=6, verbose_name='n')
    pin = models.CharField(max_length=6, verbose_name='Диаметр шпилек')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 5'
        verbose_name_plural = 'АТК 24.200.02-90 исполнение 5'

    def __str__(self):
        return self.dn_passage


class Atk24200FlangeStoppersDrawing(models.Model):
    """Чертежи для заглушек АТК 24.200.02-90"""
    execution_fl = models.CharField(max_length=6, verbose_name='Исполнение заглушки')
    execution_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'чертежи заглушек'
        verbose_name_plural = 'АТК 24.200.02-90 заглушки чертежи'

    def __str__(self):
        return self.execution_fl


class Atk2618FlangeStoppersExec1(models.Model):
    """Размеры "Исполнение 1" для заглушек ПОВОРОТНЫХ АТК 26-18-5-93"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    d2_lower = models.CharField(max_length=6, verbose_name='d2')
    a = models.CharField(max_length=6, verbose_name='A')
    b = models.CharField(max_length=6, verbose_name='B')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 1'
        verbose_name_plural = 'АТК 26-18-5-93 исполнение 1'

    def __str__(self):
        return self.dn_passage


class Atk2618FlangeStoppersExec2(models.Model):
    """Размеры "Исполнение 2" для заглушек ПОВОРОТНЫХ АТК 26-18-5-93"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1 = models.CharField(max_length=6, verbose_name='D1')
    d2 = models.CharField(max_length=6, verbose_name='D2')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    d2_lower = models.CharField(max_length=6, verbose_name='d2')
    a = models.CharField(max_length=6, verbose_name='A')
    b = models.CharField(max_length=6, verbose_name='B')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h1_lower = models.CharField(max_length=6, verbose_name='h1')
    h2_lower = models.CharField(max_length=6, verbose_name='h2')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 2'
        verbose_name_plural = 'АТК 26-18-5-93 исполнение 2'

    def __str__(self):
        return self.dn_passage


class Atk2618FlangeStoppersExec3(models.Model):
    """Размеры "Исполнение 3" для заглушек ПОВОРОТНЫХ АТК 26-18-5-93"""
    dn_passage = models.IntegerField(verbose_name='Dу')
    pn = models.FloatField(verbose_name='Ру')
    d = models.CharField(max_length=6, verbose_name='D')
    d1_lower = models.CharField(max_length=6, verbose_name='d1')
    d2_lower = models.CharField(max_length=6, verbose_name='d2')
    d3_lower = models.CharField(max_length=6, verbose_name='d3')
    a = models.CharField(max_length=6, verbose_name='A')
    b = models.CharField(max_length=6, verbose_name='B')
    b_lower = models.CharField(max_length=6, verbose_name='b')
    b1_lower = models.CharField(max_length=6, verbose_name='b1')
    b2_lower = models.CharField(max_length=6, verbose_name='b2')
    h_lower = models.CharField(max_length=6, verbose_name='h')
    h3_lower = models.CharField(max_length=6, verbose_name='h3')
    r = models.CharField(max_length=6, verbose_name='r')
    d_lower = models.CharField(max_length=6, verbose_name='d')
    m = models.CharField(max_length=6, verbose_name='Масса')

    class Meta:
        verbose_name = 'исполнение 3'
        verbose_name_plural = 'АТК 26-18-5-93 исполнение 3'

    def __str__(self):
        return self.dn_passage


class Atk2618FlangeStoppersDrawing(models.Model):
    """Чертежи для заглушек ПОВОРОТНЫХ АТК 26-18-5-93"""
    execution_fl = models.CharField(max_length=6, verbose_name='Исполнение заглушки поворотной')
    execution_drawing = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Чертеж')

    class Meta:
        verbose_name = 'чертежи заглушек поворотных'
        verbose_name_plural = 'АТК 26-18-5-93 заглушки поворотные чертежи'

    def __str__(self):
        return self.execution_fl
