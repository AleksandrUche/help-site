from gost.dataclasses import Gost28759Request
from gost.models import Gost28759FlangeValues, Gost28759FlangeMass, Gost28759FlangeDrawing


class Gost28759Handler:
    FIELDS_EXECUTION = {
        '1': ['dn_passage', 'pn', 'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 's', 'b_lower', 'h', 'd_lower', 'pin',
              'quantity_pin'],
        '2': ['dn_passage', 'pn', 'd1', 'd2', 'd5', 'd6', 'd7', 's', 'b_lower', 'h', 'd_lower', 'pin',
              'quantity_pin'],
        '3': ['dn_passage', 'pn', 'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 's', 'b_lower', 'h', 'a_lower', 'd_lower',
              'pin', 'quantity_pin'],
        '4': ['dn_passage', 'pn', 'd1', 'd2', 'd5', 'd6', 'd7', 's', 'b_lower', 'h', 'a1_lower', 'd_lower',
              'pin', 'quantity_pin'],
        '5': ['dn_passage', 'pn', 'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 's', 'b_lower', 'h', 'd_lower', 'pin',
              'quantity_pin'],
        '6': ['dn_passage', 'pn', 'd1', 'd2', 'd5', 'd6', 'd7', 's', 'b_lower', 'h', 'd_lower', 'pin',
              'quantity_pin'],
        '7': ['dn_passage', 'pn', 'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 's', 'b_lower', 'h', 'a_lower', 'd_lower', 'pin',
              'quantity_pin'],
        '8': ['dn_passage', 'pn', 'd1', 'd2', 'd4', 'd5', 'd6', 'd7', 's', 'b_lower', 'h', 'a1_lower', 'd_lower', 'pin',
              'quantity_pin'],
    }

    def __init__(self, request_data: Gost28759Request):
        self.request_data = request_data

    @property
    def flange_data(self):
        return Gost28759FlangeValues.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def drawing_flange_execution(self):
        return Gost28759FlangeDrawing.objects.filter(execution_fl=self.request_data.execution)

    @property
    def mass_flange(self):
        return Gost28759FlangeMass.objects \
            .filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn) \
            .values_list(f'exec_{self.request_data.execution}', flat=True) \
            .first()

    @property
    def fields_exec(self):
        return self.FIELDS_EXECUTION[self.request_data.execution]
