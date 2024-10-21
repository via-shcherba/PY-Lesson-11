balance = 0.0
purchase_history = []

def load_balance():
    try:
        with open('balance.txt', 'r') as file:
            return float(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0  # Возвращаем 0.0, если файл не найден или некорректный формат

def save_balance():
    with open('balance.txt', 'w') as file:
        file.write(f'{balance:.2f}')

def load_purchase_history():
    try:
        with open('purchase_history.txt', 'r') as file:
            for line in file:
                if len(line) > 1:
                    item, amount = line.strip().split(': ')
                    purchase_history.append((item, float(amount)))
    except FileNotFoundError:
        pass  

def save_purchase_history():
    with open('purchase_history.txt', 'w') as file:
        for item, amount in purchase_history:
            file.write(f'{item}: {amount:.2f}\n')

def main_menu():
    global balance
    balance = load_balance()  # Загружаем баланс при старте
    load_purchase_history()  # Загружаем историю покупок при старте

    print(f'Ваш текущий баланс: {balance:.2f}')  # Показываем баланс при открытии программы

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            deposit()
        elif choice == '2':
            make_purchase()
        elif choice == '3':
            show_purchase_history()
        elif choice == '4':
            save_balance()  # Сохраняем баланс перед выходом
            save_purchase_history()  # Сохраняем историю перед выходом
            print('Выход из программы.')
            break
        else:
            print('Неверный пункт меню, попробуйте снова.')

def deposit():
    global balance
    try:
        amount = float(input('Введите сумму для пополнения счета: '))
        if amount > 0:
            balance += amount
            print(f'Ваш счет успешно пополнен. Текущий баланс: {balance:.2f}')
        else:
            print('Сумма должна быть положительной.')
    except ValueError:
        print('Неверный ввод. Введите числовое значение.')

def make_purchase():
    global balance, purchase_history
    try:
        amount = float(input('Введите сумму покупки: '))
        if amount > balance:
            print('Недостаточно средств на счете.')
        else:
            item = input('Введите название покупки: ')
            balance -= amount
            purchase_history.append((item, amount))
            print(f'Покупка "{item}" на сумму {amount:.2f} успешно выполнена.')
            print(f'Текущий баланс: {balance:.2f}')
    except ValueError:
        print('Неверный ввод. Введите числовое значение.')

def show_purchase_history():
    if purchase_history:
        print('\nИстория покупок:')
        for i, (item, amount) in enumerate(purchase_history, 1):
            print(f'{i}. {item}: {amount:.2f}')
    else:
        print('История покупок пуста.')

def bank_account():
    print("Запуск банковского счёта...")
    main_menu()

bank_account() 