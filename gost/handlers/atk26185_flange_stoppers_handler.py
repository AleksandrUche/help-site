from gost.dataclasses import Atk26185FlangeStoppersRequest
from gost.models import Atk2618FlangeStoppersDrawing
from gost.services.services import load_class_db


class Atk26185FlangeStoppersHandler:
    def __init__(self, request_data: Atk26185FlangeStoppersRequest):
        self.request_data = request_data
        self.objects_exec_fl = load_class_db(f'Atk2618FlangeStoppersExec{self.request_data.execution}')

    @property
    def flange_data(self):
        return self.objects_exec_fl.objects.filter(dn_passage=self.request_data.dn_passage, pn=self.request_data.pn)

    @property
    def drawing_flange_execution(self):
        return Atk2618FlangeStoppersDrawing.objects.filter(execution_fl=self.request_data.execution)

    @property
    def fields_execution(self):
        return [field.name for field in self.objects_exec_fl._meta.get_fields()][1:]
