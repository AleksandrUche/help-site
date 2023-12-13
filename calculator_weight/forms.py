from django import forms

# Плотность стали
MATERIAL = [
    (7850, 'Сталь'),
    (2700, 'Алюминий'),
    (7000, 'Чугун'),
    (7900, 'Нержавейка'),
]


class BaseCalculatorForm(forms.Form):
    """Базовые поля для всех форм"""
    length = forms.DecimalField(label='Длина, метры', max_digits=10, decimal_places=1)
    material = forms.ChoiceField(label='Материал', choices=MATERIAL)


class CornerEqualShelvesWeightForm(BaseCalculatorForm):
    """Форма для расчета массы уголков равнополочных"""
    side = forms.DecimalField(label='Сторона уголка, a', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина уголка, s', max_digits=10, decimal_places=1)
    field_order = ['side', 'thickness']


class CornerDifferentShelvesWeightForm(CornerEqualShelvesWeightForm):
    """Форма для расчета массы уголков не равнополочных"""
    side_b = forms.DecimalField(label='Сторона уголка, b', max_digits=10, decimal_places=1)
    field_order = ['side', 'side_b', 'thickness']


class CircleForm(BaseCalculatorForm):
    """Форма для расчета массы кругляка"""
    diameter = forms.DecimalField(label='Диаметр, d', max_digits=10, decimal_places=1)
    field_order = ['diameter']


class SquareForm(BaseCalculatorForm):
    """Форма для расчета массы квадрата"""
    size = forms.DecimalField(label='Сторона квадрата, a', max_digits=10, decimal_places=1)
    field_order = ['size']


class SheetForm(BaseCalculatorForm):
    """Форма для расчета массы листа"""
    side_a = forms.DecimalField(label='Ширина листа, a', max_digits=10, decimal_places=1)
    side_b = forms.DecimalField(label='Длина листа, b', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина листа, s', max_digits=10, decimal_places=1)
    length = None  # Исключил
    field_order = ['side_a', 'side_b', 'thickness']


class TubeForm(BaseCalculatorForm):
    """Форма для расчета массы трубы"""
    diameter = forms.DecimalField(label='Диаметр, d', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина, s', max_digits=10, decimal_places=1)
    field_order = ['diameter', 'thickness']


class ProfileTubeForm(BaseCalculatorForm):
    """Форма для расчета массы профильной трубы"""
    side_a = forms.DecimalField(label='Ширина трубы, a', max_digits=10, decimal_places=1)
    side_b = forms.DecimalField(label='Высота трубы, b', max_digits=10, decimal_places=1)
    thickness = forms.DecimalField(label='Толщина, s', max_digits=10, decimal_places=1)
    field_order = ['side_a', 'side_b', 'thickness']


# Поле выбора типа швеллера
CHANNEL = [
    (None, 'Выберите тип'),
    ('ChannelTypeY', 'С уклоном внутренних граней полок "У"'),
    ('ChannelTypeP', 'С параллельными гранями полок "П"'),
    ('ChannelTypeE', 'Экономичные с параллельными гранями полок "Э"'),
    ('ChannelTypeL', 'Легкой серии с параллельными гранями полок "Л"'),
    ('ChannelTypeC', 'Специальные "C"')
]


class ChannelForm(forms.Form):
    """Форма для расчета массы швеллера"""
    type = forms.ChoiceField(label='Тип швеллера', choices=CHANNEL)
    name = forms.CharField(label='Номер швеллера', widget=forms.Select)
    length = forms.DecimalField(label='Длина, мм', max_digits=10, decimal_places=1)


# Поле выбора типа двутавра
BEAM = [
    (None, 'Выберите тип'),
    ('BeamGost8239', 'Двутавр с уклоном полок'),
    ('BeamGost26020TypeB', 'Нормальный двутавр "Б"'),
    ('BeamGost26020TypeSh', 'Широкополочный двутавр "Ш"'),
    ('BeamGost26020TypeK', 'Колонный двутавр "К"'),
    ('BeamGost26020TypeD', 'Двутавр дополнительной серии "Д"'),
    ('BeamGost26020TypeS', 'Сварной двутавр "С"')
]


class BeamForm(forms.Form):
    """Форма для расчета массы двутавра"""
    type = forms.ChoiceField(label='Тип двутавра', choices=BEAM)
    name = forms.CharField(label='Номер двутавра', widget=forms.Select)
    length = forms.DecimalField(label='Длина, мм', max_digits=10, decimal_places=1)
