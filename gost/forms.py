from django import forms


class Gost33259Form(forms.Form):  # Фланцы ГОСТ 33259-2017
    TYPE_FL = (
        (None, 'Выберите тип'),
        ('01', 'Тип 01'),
        ('02', 'Тип 02'),
        ('11', 'Тип 11'),
    )
    SURFACE = (
        # (None, 'Выберите поверхность'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    type_fl = forms.ChoiceField(label='Тип фланца', choices=TYPE_FL)
    surface = forms.ChoiceField(label='Уплотнительная поверхность', choices=SURFACE)
    dn_passage = forms.CharField(label='DN')
    pn = forms.CharField(label='PN')


class Atk261813Form(forms.Form):  # Фланцы АТК
    EXECUTION = (
        (None, 'Выберите исполнение'),
        ('1', 'Исполнение 1'),
        ('2', 'Исполнение 2'),
        ('3', 'Исполнение 3'),
        ('4', 'Исполнение 4'),
        ('5', 'Исполнение 5'),
        ('6', 'Исполнение 6'),
    )
    execution = forms.ChoiceField(label='Исполнение', choices=EXECUTION)
    pn = forms.CharField(label='Py, МПа')
    dn_passage = forms.CharField(label='Dy')


class Gost6533Form(forms.Form):  # Днища
    DRAWING = (
        (None, 'Выберите чертеж'),
        ('1', 'Чертеж 1'),
        ('2', 'Чертеж 2'),
        ('3', 'Чертеж 3'),
    )
    drawing = forms.ChoiceField(label='Чертеж', choices=DRAWING)
    diameter = forms.CharField(label='Диаметр')
    thickness = forms.CharField(label='Толщина, s')


class Atk24200FlangeStoppersForm(forms.Form):  # Заглушки АТК обычные
    EXECUTION = (
        (None, 'Выберите исполнение'),
        ('1', 'Исполнение 1'),
        ('2', 'Исполнение 2'),
        ('3', 'Исполнение 3'),
        ('4', 'Исполнение 4'),
        ('5', 'Исполнение 5'),
    )
    execution = forms.ChoiceField(label='Исполнение', choices=EXECUTION)
    pn = forms.CharField(label='Py, МПа')
    dn_passage = forms.CharField(label='Dy')


class Atk26185FlangeStoppersForm(forms.Form):  # Заглушки АТК (ПОВОРОТНЫЕ)
    EXECUTION = (
        (None, 'Выберите исполнение'),
        ('1', 'Исполнение 1'),
        ('2', 'Исполнение 2'),
        ('3', 'Исполнение 3'),
    )
    execution = forms.ChoiceField(label='Исполнение', choices=EXECUTION)
    pn = forms.CharField(label='Py, МПа')
    dn_passage = forms.CharField(label='Dy')

