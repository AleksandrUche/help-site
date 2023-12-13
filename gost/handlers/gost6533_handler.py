from gost.dataclasses import Gost6533Request
from gost.models import Gost6533Bottoms, Gost6533BottomsDrawing


class Gost6533Handler:
    def __init__(self, request_data: Gost6533Request):
        self.request_data = request_data

    @property
    def field_values(self):
        return [field.name for field in Gost6533Bottoms._meta.get_fields()][2:]

    @property
    def bottom_data(self):
        return Gost6533Bottoms.objects.filter(
            exec=self.request_data.drawing,
            d=self.request_data.diameter,
            s_lower=self.request_data.thickness,
        )

    @property
    def drawing_bottom(self):
        return Gost6533BottomsDrawing.objects.filter(execution=self.request_data.drawing)
