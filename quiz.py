import random

people = {
    'Albert Einstein': '14.03.1879',
    'Marie Curie': '07.11.1867',
    'Isaac Newton': '04.01.1643',
    'Galileo Galilei': '15.02.1564',
    'Leonardo da Vinci': '15.04.1452',
    'Nikola Tesla': '10.07.1856',
    'Ada Lovelace': '10.12.1815',
    'Charles Darwin': '12.02.1809',
    'Wolfgang Mozart': '27.01.1756',
    'William Shakespeare': '23.04.1564'
}

def date_to_text(date):
    days = {
        '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое',
        '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое',
        '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое',
        '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
        '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое',
        '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое',
        '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое',
        '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
    }
    months = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
        '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
        '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    day, month, year = date.split('.')
    return f"{days[day]} {months[month]} {year} года"

def start_quiz():
    random_people = random.sample(list(people.keys()), 5)
    correct_answers = 0

    for person in random_people:
        user_answer = input(f"Введите дату рождения {person} (в формате dd.mm.yyyy): ")
        correct_date = people[person]

        if user_answer == correct_date:
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно. Правильный ответ: {date_to_text(correct_date)}")

    total_questions = len(random_people)
    incorrect_answers = total_questions - correct_answers
    correct_percentage = (correct_answers * 100) / total_questions
    incorrect_percentage = 100 - correct_percentage

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

    # Ask the user if they want to play again
    play_again = input("\nХотите начать игру сначала? (да/нет): ").strip().lower()
    if play_again == 'да':
        start_quiz()
    else:
        print("Спасибо за игру!")


def play_quiz():
    print("Запуск викторины...")
    start_quiz()