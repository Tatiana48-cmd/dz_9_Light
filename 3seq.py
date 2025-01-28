# Ввод элементов 1-го списка
first_input = input("Введите элементы 1-го списка через запятую, точку с запятой или слэш: ")

# Определяем разделитель для 1-го списка
if "," in first_input:
    delimiter = ","
elif ";" in first_input:
    delimiter = ";"
elif "/" in first_input:
    delimiter = "/"
else:
    print("Ошибка: используйте один из разделителей — запятую, точку с запятой или слэш.")
    exit()

# Преобразуем 1-й список в список чисел
first_list = [int(x.strip()) for x in first_input.split(delimiter)]

# Ввод элементов 2-го списка
second_input = input("Введите элементы 2-го списка через запятую, точку с запятой или слэш: ")

# Определяем разделитель для 2-го списка
if delimiter not in second_input:
    print(f"Ошибка: используйте тот же разделитель ({delimiter}) для ввода 2-го списка.")
    exit()

# Преобразуем 2-й список в список чисел
second_list = [int(x.strip()) for x in second_input.split(delimiter)]

# Удаляем из 1-го списка элементы, присутствующие во 2-м
result_list = [x for x in first_list if x not in second_list]

# Вывод результата
print("Результат:", ", ".join(map(str, result_list)))
