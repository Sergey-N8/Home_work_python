# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = 10 # колличество элементов в прогрессии

a1 = 2 # первый элемент прогрессии

d = 5 # Разность, шаг прогрессии

list_1 = [i for i in range(a1, (a1 + n * d), d)]

print(list_1)

for i in range(n):
    print(a1 + i * d)