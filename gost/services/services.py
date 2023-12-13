import importlib


def load_class_db(name_cls):
    """Загружает однотипные модели"""
    module_path = 'gost.models'
    module = importlib.import_module(module_path)
    return getattr(module, name_cls)
