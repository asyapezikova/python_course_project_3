from utils import *

file_json = "../files_json/operations.json"

def main():
    try:
        operations_list = uploading_a_file(file_json)
        operations = get_finished_five(conversion_of_operations(operations_list))
        print(operations)
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()