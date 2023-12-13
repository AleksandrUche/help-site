from gost.dataclasses import Atk261813Request
from gost.models import Atk261813FlangeDrawing
from gost.services.services import load_class_db


class Atk261813Handler:
    def __init__(self, request_data: Atk261813Request):
        self.request_data = request_data
        self.objects_exec_fl = load_class_db(f'Atk261813FlangeExec{self.request_data.execution}')

    @property
    def flange_data(self):
        """Размеры фланца"""
        return self.objects_exec_fl.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def drawing_flange_execution(self):
        """Чертеж исполнения"""
        return Atk261813FlangeDrawing.objects.filter(execution_fl=self.request_data.execution)

    @property
    def fields_execution(self):
        """Поля выбранного исполнения из БД"""
        return [field.name for field in self.objects_exec_fl._meta.get_fields()][1:]
