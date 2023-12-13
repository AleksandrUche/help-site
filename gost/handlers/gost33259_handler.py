from gost.dataclasses import Gost33259Request
from gost.models import (
    Gost33259TypeDrawing,
    Gost33259SurfaceDrawing,
    Gost33259SurfaceValues,
    Gost33259Mass,
)
from gost.services.services import load_class_db


class Gost33259Handler:
    # Значения (уплотнительной поверхность) которые необходимо вывести при выборе ряда 1 и ряда 2
    FIELDS_SURFACE_FL = {
        '1': {
            'B': ['h_lower', 'd2'],
            'C': ['h1_lower', 'd3_row_one', 'd4_row_one'],
            'D': ['h_lower', 'h2_lower', 'd2', 'd6_row_one', 'd5_row_one'],
            'E': ['h1_lower', 'd4_row_one'],
            'F': ['h_lower', 'h2_lower', 'd2', 'd6_row_one'],
        },
        '2': {
            'B': ['h_lower', 'd2'],
            'C': ['h1_lower', 'd3_row_two', 'd4_row_two'],
            'D': ['h_lower', 'h2_lower', 'd2', 'd6_row_two', 'd5_row_two'],
            'E': ['h1_lower', 'd4_row_two'],
            'F': ['h_lower', 'h2_lower', 'd2', 'd6_row_two'],
        }
    }
    # Значения (основные размеры) которые нужно вывести при выборе ряда 1 и ряда 2
    FIELDS_TYPE_FL = {
        'Gost33259Type01': {
            '1': ['dn_passage', 'pn', 'dv_lower_row_one', 'b_lower_row_one', 'c1_lower', 'd_row_one', 'd1',
                  'd_lower_row_one', 'n_lower_row_one', 'pin_row_one'],
            '2': ['dn_passage', 'pn', 'dv_lower_row_two', 'b_lower_row_two', 'c1_lower', 'd_row_two', 'd1',
                  'd_lower_row_two', 'n_lower_row_two', 'pin_row_two']
        },
        'Gost33259Type02': {
            '1': ['dn_passage', 'pn', 'd0_row_one', 'd2', 'dv_lower_row_one', 'b_lower_row_one', 'b1_lower_row_one',
                  'c_lower_row_one', 'c1_lower', 'd_row_one', 'd1', 'd_lower_row_one', 'n_lower_row_one',
                  'pin_row_one'],
            '2': ['dn_passage', 'pn', 'd0_row_two', 'd2', 'dv_lower_row_two', 'b_lower_row_two', 'b1_lower_row_two',
                  'c_lower_row_two', 'c1_lower', 'd_row_two', 'd1', 'd_lower_row_two', 'n_lower_row_two',
                  'pin_row_two']
        },
        'Gost33259Type11': {
            '1': ['dn_passage', 'pn', 'dm_row_one', 'dn_row_one', 'd1_lower_row_one', 'b_lower_row_one',
                  'h_row_one', 'h1', 'd_row_one', 'd1', 'd_lower_row_one', 'n_lower_row_one', 'pin_row_one'],
            '2': ['dn_passage', 'pn', 'dm_row_two', 'dn_row_two', 'd1_lower_row_two', 'b_lower_row_two',
                  'h_row_two', 'h1', 'd_row_two', 'd1', 'd_lower_row_two', 'n_lower_row_two', 'pin_row_two']
        }
    }

    def __init__(self, request_data: Gost33259Request):
        self.request_data = request_data
        self.objects_types_fl = load_class_db(f'Gost33259Type{self.request_data.type_fl}')

    @property
    def flange_data(self):
        """Значения для определенного типа фланца"""
        return self.objects_types_fl.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def drawing_flange_type(self):
        """Чертеж определенного типа фланца"""
        return Gost33259TypeDrawing.objects.filter(type_fl=self.request_data.type_fl)

    @property
    def drawing_flange_surface(self):
        """Чертеж уплотнительной поверхности"""
        return Gost33259SurfaceDrawing.objects.filter(surface_fl=self.request_data.surface)

    @property
    def fields_surface_flange(self):
        """Поля для уплотнительной поверхности фланца"""
        return self.FIELDS_SURFACE_FL[self.request_data.row][self.request_data.surface]

    @property
    def fields_type_flange(self):
        """Поля для фланца по типам (основные размеры)"""
        return self.FIELDS_TYPE_FL[f'Gost33259Type{self.request_data.type_fl}'][self.request_data.row]

    @property
    def surface_data(self):
        """Значения уплотнительной поверхности"""
        return Gost33259SurfaceValues.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def mass_flange(self):
        """
        Масса фланца
        При возвращении None в шаблоне будет отображено "Масса не указана"
        """
        # Для давления 2.5 поиск в БД идет по колонке pn_2
        if self.request_data.pn == '2.5':
            self.request_data.pn = '2'

        mass = Gost33259Mass.objects \
            .filter(dn_passage=self.request_data.dn_passage, type_fl=self.request_data.type_fl)\
            .first()

        if mass:
            return getattr(mass, f'pn_{self.request_data.pn}')


# return Gost33259Mass.objects \
#                 .filter(dn_passage=self.request_data.dn_passage, type_fl=self.request_data.type_fl) \
#                 .values_list(f'pn_{self.request_data.pn}', flat=True).get()
