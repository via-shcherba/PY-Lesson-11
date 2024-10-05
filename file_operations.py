import os
import shutil

def create_folder():
    folder_name = input("Введите название папки: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"Папка '{folder_name}' была создана.")

def delete_item():
    item_name = input("Введите название файла/папки для удаления: ")
    try:
        if os.path.isdir(item_name):
            os.rmdir(item_name)
        else:
            os.remove(item_name)
        print(f"'{item_name}' был удален.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")

def copy_item():
    src = input("Введите название файла/папки для копирования: ")
    dst = input("Введите новое название для копии: ")
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)
        print(f"'{src}' был скопирован в '{dst}'.")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")

def list_directory_contents():
    print("Содержимое рабочей директории:")
    for item in os.listdir():
        print(item)

def list_directories():
    print("Папки в рабочей директории:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

def list_files():
    print("Файлы в рабочей директории:")
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

def change_working_directory():
    new_dir = input("Введите новый путь к рабочей директории: ")
    try:
        os.chdir(new_dir)
        print(f"Рабочая директория изменена на: {os.getcwd()}")
    except Exception as e:
        print(f"Ошибка при изменении директории: {e}")