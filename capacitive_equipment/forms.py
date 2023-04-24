from django import forms
from capacitive_equipment.models import NameCapacitiveEquipment, Parameter


class AddNameCapacEquipmentForm(forms.ModelForm):
    class Meta:
        model = NameCapacitiveEquipment
        fields = ['name_equipment', 'type_equipment', 'calc_number']


class AddParameterCapacEquipmentForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = [
            # 'id', 'calculation_id',
            'support_capacitive_device', 'support_capacitive_device_quantity',
            'thermal_insulation', 'thermal_insulation_quantity', 'thermal_insulation_type',
            'overlays_service_platform', 'ladder', 'hydrogen_sulfide', 'hydrogen_sulfide_group', 'corrosion',
            'service_life', 'heat_treatment', 'working_temperature', 'calculated_temperature', 'design_pressure',
            'density', 'steaming_temperature', 'seismic_activity', 'coating_external', 'coating_internal',
            'conservation_requirement', 'visual_identification', 'spare_parts', 'departures_fittings',
            'flange_coils', 'rotary_fl_stoppers'
        ]
