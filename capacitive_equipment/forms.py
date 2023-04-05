from django import forms
from capacitive_equipment.models import NameCapacitiveEquipment


class AddCapacEquipmentForm(forms.ModelForm):
    class Meta:
        model = NameCapacitiveEquipment
        fields = ['name_equipment', 'type_equipment', 'calc_number', 'author']

