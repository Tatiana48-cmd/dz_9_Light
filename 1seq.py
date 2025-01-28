# Переменная под количество элементов списка
element_count = int(input('Введите количество элементов списка: '))
print(f"Количество элементов списка: ", element_count)

elements = []

# В цикле запрашиваем элементы и добавляем их в список
for i in range(1, element_count+1):
    element = int(input(f"Введите {i} элемент: "))
    elements.append(element)
    print(elements)

# Сортируем список по возрастанию
elements.sort()

# Выводим отсортированный список
print("Отсортированный список:", elements)