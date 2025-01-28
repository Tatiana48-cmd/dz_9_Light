import random
from datetime import datetime

# Словарь с именами известных людей и их датами рождения
people_birthdays = {
    "Валерий Харламов": "14.01.1948",
    "А. П. Чехов": "29.01.1860",
    "Чарльз Диккенс": "07.02.1812",
    "Владимир Высоцкий": "25.01.1938",
    "Шерон Стоун": "10.03.1958",
    "Джекки Чан": "07.04.1954",
    "Сильвестр Сталлоне": "06.06.1946",
    "Анна Ахматова": "23.06.1889",
    "Юрий Гагарин": "09.03.1934",
    "Святослав Рихтер": "20.03.1915",
}

while True:
    correct_answers = 0
    incorrect_answers = 0

    # Выбираем 5 случайных людей
    selected_people = random.sample(list(people_birthdays.items()), 5)

    # Задаем вопросы пользователю
    for name, birthday in selected_people:
        print(f"Когда родился {name}?")
        user_input = input("Введите дату в формате 'dd.mm.yyyy': ")

        if user_input == birthday:
            print("Верно!")
            correct_answers += 1
        else:
            months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
            date_obj = datetime.strptime(birthday, "%d.%m.%Y")
            day = date_obj.day
            month = months[date_obj.month - 1]
            year = date_obj.year
            formatted_birthday = f"{day} {month} {year} года"
            print(f"Неверно. Правильный ответ: {formatted_birthday}")
            incorrect_answers += 1

    # Итоги игры
    print(f"\nПравильных ответов: {correct_answers}")
    print(f"Неправильных ответов: {incorrect_answers}")

    # Предложение начать заново
    play_again = input("Хотите сыграть снова? (да/нет): ").strip().lower()
    if play_again != "да":
        print("Спасибо за игру!")
        break
