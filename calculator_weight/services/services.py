import importlib


def load_class_db(name_cls):
    module_path = 'calculator_weight.models'
    module = importlib.import_module(module_path)
    return getattr(module, name_cls)
