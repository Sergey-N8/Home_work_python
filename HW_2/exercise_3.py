# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


namber = int(input('Введите число N: '))

result = 1

while result * 2 <= namber:
    print(result)
    result *= 2

print(result)
