from django import forms
from gost.models import Gost28759FlangeValues


class Gost33259Form(forms.Form):
    """Форма для фланцев по ГОСТ 33259-2017"""
    TYPE_FL = (
        (None, 'Выберите тип'),
        ('01', 'Тип 01'),
        ('02', 'Тип 02'),
        ('11', 'Тип 11'),
    )
    SURFACE = (
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    type_fl = forms.ChoiceField(label='Тип фланца', choices=TYPE_FL)
    surface = forms.ChoiceField(label='Уплотнительная поверхность', choices=SURFACE)
    dn_passage = forms.CharField(label='DN', widget=forms.Select)
    pn = forms.CharField(label='PN, кгс/см^2', widget=forms.Select)
    row = forms.ChoiceField(label='Ряд', choices=[(1, 'Ряд 1'), (2, 'Ряд 2')])


class Gost28759Form(forms.Form):
    """Форма для фланцев по ГОСТ 28759.3—2022"""
    EXECUTION = (
        (None, 'Выберите исполнение'),
        ('1', 'Исполнение 1'),
        ('2', 'Исполнение 2'),
        ('3', 'Исполнение 3'),
        ('4', 'Исполнение 4'),
        ('5', 'Исполнение 5'),
        ('6', 'Исполнение 6'),
        ('7', 'Исполнение 7'),
        ('8', 'Исполнение 8'),
    )
    CH = ((elem, elem) for elem in Gost28759FlangeValues.objects.values_list('dn_passage', flat=True).distinct())

    execution = forms.ChoiceField(label='Исполнение', choices=EXECUTION)
    dn_passage = forms.ChoiceField(label='DN', choices=CH)
    pn = forms.CharField(label='PN, МПа', widget=forms.Select)


class Atk261813Form(forms.Form):
    """Форма для фланцев по АТК 26-18-14-98"""
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


class Gost6533Form(forms.Form):
    """Форма для днищ по ГОСТ 6533-78"""
    DRAWING = (
        (None, 'Выберите чертеж'),
        ('1', 'Чертеж 1'),
        ('2', 'Чертеж 2'),
        ('3', 'Чертеж 3'),
    )
    drawing = forms.ChoiceField(label='Чертеж', choices=DRAWING)
    diameter = forms.CharField(label='Диаметр')
    thickness = forms.CharField(label='Толщина, s')


class Atk24200FlangeStoppersForm(forms.Form):
    """Форма для заглушек по АТК 24.200.02-90"""
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


class Atk26185FlangeStoppersForm(forms.Form):
    """Форма для заглушек поворотных по АТК 26-18-5-93"""
    EXECUTION = (
        (None, 'Выберите исполнение'),
        ('1', 'Исполнение 1'),
        ('2', 'Исполнение 2'),
        ('3', 'Исполнение 3'),
    )
    execution = forms.ChoiceField(label='Исполнение', choices=EXECUTION)
    pn = forms.CharField(label='Py, МПа')
    dn_passage = forms.CharField(label='Dy')
