# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

money_namber = int(input('Колличество монет: '))

money_on_table = []

eagle_m = 0

tails_m = 0

for i in range(money_namber):
    money_pos = random.getrandbits(1)
    if money_pos == 1:
        money_on_table.append('eagle') 
        eagle_m += 1  
    else:
        money_on_table.append('tails')
        tails_m += 1  

print("\n"f'На столе лежит {money_on_table}')
print("\n"f'Что бы все монеты были повернуты в одну сторону, необходимо повернуть {min([eagle_m,tails_m])} монет') 


#{(eagle_m < tails_m) * eagle_m + (eagle_m > tails_m) * tails_m} 

