from django import forms

MATERIAL = [
    (7850, 'Сталь'),
    (2700, 'Алюминий'),
    (7000, 'Чугун'),
    (7900, 'Нержавейка'),
]


class BaseCalculatorForm(forms.Form):
    length = forms.DecimalField(label='Длина, L', max_digits=10, decimal_places=1)
    material = forms.ChoiceField(label='Материал', choices=MATERIAL)


class CornerEqualShelvesWeightForm(BaseCalculatorForm):
    side = forms.DecimalField(label='Сторона уголка, a', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина уголка, s', max_digits=10, decimal_places=1)
    field_order = ['side', 'thickness']


class CornerDifferentShelvesWeightForm(CornerEqualShelvesWeightForm):
    side_b = forms.DecimalField(label='Сторона уголка, b', max_digits=10, decimal_places=1)
    field_order = ['side', 'side_b', 'thickness']


class CircleForm(BaseCalculatorForm):
    diameter = forms.DecimalField(label='Диаметр, d', max_digits=10, decimal_places=1)
    field_order = ['diameter']


class SquareForm(BaseCalculatorForm):
    size = forms.DecimalField(label='Сторона квадрата, a', max_digits=10, decimal_places=1)
    field_order = ['size']


class SheetForm(BaseCalculatorForm):
    side_a = forms.DecimalField(label='Ширина листа, a', max_digits=10, decimal_places=1)
    side_b = forms.DecimalField(label='Длина листа, b', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина листа, s', max_digits=10, decimal_places=1)
    length = None  # Исключил
    field_order = ['side_a', 'side_b', 'thickness']


class TubeForm(BaseCalculatorForm):
    diameter = forms.DecimalField(label='Диаметр, d', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина, s', max_digits=10, decimal_places=1)
    field_order = ['diameter', 'thickness']


class ProfileTubeForm(BaseCalculatorForm):
    side_a = forms.DecimalField(label='Ширина трубы, a', max_digits=10, decimal_places=1)
    side_b = forms.DecimalField(label='Высота трубы, b', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина, s', max_digits=10, decimal_places=1)
    field_order = ['side_a', 'side_b', 'thickness']


class ChannelForm(forms.Form):
    pass


class BeamForm(forms.Form):
    pass
