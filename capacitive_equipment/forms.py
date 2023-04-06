from django import forms
from capacitive_equipment.models import NameCapacitiveEquipment, Parameter


class AddNameCapacEquipmentForm(forms.ModelForm):
    class Meta:
        model = NameCapacitiveEquipment
        fields = ['name_equipment', 'type_equipment', 'calc_number', 'author']


class AddParameterCapacEquipmentForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = '__all__'
