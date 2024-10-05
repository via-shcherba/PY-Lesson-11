from file_operations import create_folder, delete_item, copy_item, list_directory_contents, list_directories, list_files, change_working_directory
from system_info import os_info, program_creator
from quiz import play_quiz
from bank_account import bank_account

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            list_directory_contents()
        elif choice == '5':
            list_directories()
        elif choice == '6':
            list_files()
        elif choice == '7':
            os_info()
        elif choice == '8':
            program_creator()
        elif choice == '9':
            play_quiz()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            change_working_directory()
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неправильный ввод. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main_menu()