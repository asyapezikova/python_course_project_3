import src.operations
from src.utils import *

test_file_json = "../files_json/test_operation.json"

def tests_files_json():
    assert type(uploading_a_file(test_file_json)) is list

def tests_conversion_of_operations():
    test_operations_list = uploading_a_file(test_file_json)

    for obj in conversion_of_operations(test_operations_list):
        assert type(obj) is src.operations.Operation

    assert conversion_of_operations(test_operations_list)[0].get_date() == "26.08.2019"
    assert conversion_of_operations(test_operations_list)[0].get_state() == "EXECUTED"
    assert conversion_of_operations(test_operations_list)[6].get_state() == "CANCELED"
    assert str(conversion_of_operations(test_operations_list)[0]) == "26.08.2019 Перевод организации\n" \
                                                                "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                                                "31957.58 руб.\n\n"
    assert conversion_of_operations(test_operations_list)[0].__repr__() == "26.08.2019 Перевод организации\n" \
                                                                     "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                                                     "31957.58 руб.\n\n"

def test_get_finished_five():
    test_operations_list = uploading_a_file(test_file_json)
    obj = conversion_of_operations(test_operations_list)
    assert str(get_finished_five(obj)) == "26.08.2019 Перевод организации\n" \
                                         "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                         "31957.58 руб.\n\n" \
                                         "03.07.2019 Перевод организации\n" \
                                         "MasterCard 7158 30** **** 6758 -> Счет **5560\n" \
                                         "8221.37 USD\n\n" \
                                         "04.04.2019 Перевод со счета на счет\n" \
                                         "Счет **8542 -> Счет **4188\n" \
                                         "79114.93 USD\n\n" \
                                         "23.03.2019 Перевод со счета на счет\n" \
                                         "Счет **4719 -> Счет **1160\n" \
                                         "43318.34 руб.\n\n" \
                                         "30.06.2018 Перевод организации\n" \
                                         "Счет **6952 -> Счет **6702\n" \
                                         "9824.07 USD\n\n"
