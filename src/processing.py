from typing import Any


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая принимает список словарей по ключу state
    и возвращает список словарей, содержащих данный ключ"""
    filter_list = []
    for i in list_dict:
        if i.get("state") == state:
            filter_list.append(i)
    return filter_list


def sort_by_date(input_list: list[Any], descending=True) -> Any:
    """Функция сортировки операций по дате
    @rtype: object
    """
    if len(input_list) > 0:
        sorted_list = sorted(
            input_list, key=lambda x: x.get("date"), reverse=descending
        )
        return sorted_list
    else:
        return "Список пуст"
