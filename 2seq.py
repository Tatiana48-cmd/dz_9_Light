# Ввод данных от пользователя
user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")
print(user_input)

# Определяем используемый разделитель
if "," in user_input:
    delimiter = ","
elif ";" in user_input:
    delimiter = ";"
elif "/" in user_input:
    delimiter = "/"
else:
    print("Ошибка: используйте только один из разделителей — запятую, точку с запятой или слэш.")
    exit()

# Разбиваем строку на элементы и преобразуем их в числа
elements = [int(x.strip()) for x in user_input.split(delimiter)]

# Создаем новый список с уникальными элементами
unique_elements = [x for x in elements if elements.count(x) == 1]

# Вывод результата
print("Результат:", ", ".join(map(str, unique_elements)))
