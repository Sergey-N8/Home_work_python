# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

inp_max = int(input("Введите максимольно значение: "))

inp_min = int(input("Введите минимальное значение: "))

size = 20

list_1 = [random.randint(1, 100) for i in range(size)]

def max_min(list_1):
    list_result = []
    for i in range(len(list_1)):
        if inp_min < list_1[i] < inp_max:
            list_result.append(i)
    return list_result

print(list_1)
print(max_min(list_1))