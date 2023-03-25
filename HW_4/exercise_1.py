# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# list_1 = [3, 3, 1, 1, 7, 8, 9, 0, 4, 3, 2, 9, 0, 4, 3, 2]
# list_2 = [4, 8, 8, 9, 0, 4, 3, 2]

# def lists_union(list_1, list_2):
#     result_list = []
#     for i in set(list_1):
#         for j in set(list_2):
#             if j == i:
#                 result_list.append(i)
#     result_list.sort()
#     return ', '.join([str(i) for i in result_list])
# print(lists_union(list_1, list_2))

# list_1 = [int(input('Введите элемент первого массива: ')) for i in range(int(input('Введите размер первого массива: ')))]
# list_2 = [int(input('Введите элемент второго массива: ')) for i in range(int(input('Введите размер второго массива: ')))]

def enter_list(n):
    result_list = []
    for i in range(n):
        result_list.append(int(input('Введите элемент массива: ')))
    return result_list

n_1 = int(input('Введите размер первого массива: '))
n_2 = int(input('Введите размер второго массива: '))

print(', '.join([str(i) for i in (set(enter_list(n_1)) & set(enter_list(n_2)))]))
