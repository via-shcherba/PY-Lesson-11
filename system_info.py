import platform

def os_info():
    print(f"Процессор: {platform.processor()}")
    print(f"Система: {platform.system()} {platform.release()}")
    print(f"Имя машины: {platform.node()}")
    print(f"Архитектура: {platform.architecture()[0]}")

def program_creator():
    print("Создатель программы: via.shcherba")