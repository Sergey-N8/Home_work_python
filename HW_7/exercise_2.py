# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table.reduce(lambda x, y: x * y)`
# **Вывод:**

# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36



def print_operation_table(x, y):
    mas = [[0] * y for i in range(x)]
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            mas[i - 1][j - 1] = (i * j)
        print(' '.join(map(str, mas[i - 1])))

x1 = 10
y1 = 9

print_operation_table(x1, y1)

#7777777777777777777777777777777777777


# def print_operation_table(operation, num_rows=9, num_columns=9):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print(''.join(f'{e:<4}' for e in answer))

# print_operation_table(lambda x, y: x * y)