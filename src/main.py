from utils import *

def main():
    try:
        operations_list = files_json()
        operations = get_executed_five(conversion_of_operations(operations_list))
        for op in operations:
            print(op)
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()