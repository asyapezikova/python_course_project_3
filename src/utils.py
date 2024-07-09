import json
import datetime

from src.operations import Operation

def uploading_a_file(file_json):
    '''
    Получает JSON-файл и преобразует его в Python-словарь
    :return: словарь с банковскими операциями
    '''
    with open(file_json, "r", encoding="UTF-8") as json_file:
        operations = json.load(json_file)
        return operations

def conversion_of_operations(operation):
    '''
    Создает список экземпляров класса Operation
    :param operation: список с банковскими операциями
    :return: список экземпляров класса с банковскими операциями
    '''
    banking_operation_list = []
    def check_wallet(where: str):
        '''
        Функция шифрует данные кошелька, в зависимости от его типа
        :param where: получатель:to или отправитель:from
        :return: зашифрованный кошелек
        '''
        wallet = "Неизвестно"
        try:
            card = information[f'{where}']
            if card[:4] == "Счет":
                wallet = f"{card[:4]} **{card[-4:]}"
            else:
                wallet = f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"
            return wallet
        except:
            return wallet

    for information in operation:
        try:
            id = information["id"]
            state = information["state"]
            full_date = datetime.datetime.strptime(information["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date = datetime.datetime.strftime(full_date, "%d.%m.%Y")
            description = information["description"]
            where_from = check_wallet("from")
            to = check_wallet("to")
            amount = information["operationAmount"]["amount"]
            currency = information["operationAmount"]["currency"]["name"]
            banking_operation = Operation(id, state, date, description, where_from, to, amount, currency)
            banking_operation_list.append(banking_operation)
        except:
            continue
    return banking_operation_list

def get_finished_five(operations: list):
    '''
    Функция выводит последние 5 выполенных операций
    :param operations: список экземпляров класса Operations
    :return: данные с пятью последними успешными операциями
    '''
    operations_executed = ''
    num = 0
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        if operation.get_state() == "EXECUTED":
            num += 1
            operations_executed += operation.__repr__()
        if num == 5:
            break
    return operations_executed