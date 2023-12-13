from gost.dataclasses import Atk24200FlangeStoppersRequest
from gost.models import Atk24200FlangeStoppersDrawing
from gost.services.services import load_class_db


class Atk24200FlangeStoppersHandler:
    def __init__(self, request_data: Atk24200FlangeStoppersRequest):
        self.request_data = request_data
        self.objects_exec_fl = load_class_db(f'Atk24200FlangeStoppersExec{self.request_data.execution}')

    @property
    def flange_data(self):
        return self.objects_exec_fl.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def drawing_flange_execution(self):
        return Atk24200FlangeStoppersDrawing.objects.filter(execution_fl=self.request_data.execution)

    @property
    def fields_execution(self):
        return [field.name for field in self.objects_exec_fl._meta.get_fields()][1:]
