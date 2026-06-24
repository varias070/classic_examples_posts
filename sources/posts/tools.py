from typing import Any


def _unnest_init(objects, **kwargs) -> dict:
    """
    Инициализирует словарь с одинаковыми значениями,
    например id или callable для вычеслений.
    """
    result = {}
    for key, value in kwargs.items():
        if callable(value):
            result[key] = [value(item) for item in objects]
        else:
            result[key] = [value for _ in objects]
    return result


def unnest_objects(objects: list[Any], **kwargs) -> dict[str, list]:
    """Преобразует список обьектов в словарь списков значений атрибутов"""
    if not objects:
        return {}

    result = _unnest_init(objects, **kwargs)
    print(result)
    keys = objects[0].__dict__.keys()
    for key in keys:
        result[key] = [getattr(obj, key) for obj in objects]

    return result
