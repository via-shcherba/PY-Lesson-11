balance = 0.0
purchase_history = []

def main_menu():   
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


main_menu()
