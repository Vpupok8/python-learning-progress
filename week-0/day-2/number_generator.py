# Напиши программу, которая генерирует числа от 1 до 100, но:

#    Пропускает числа, кратные 3.
#    Останавливается, если число делится на 7 без остатка.
import random

while True:
    
    random_number = random.randint(1, 100)
    if random_number % 3 == 0:
        print(f'{random_number} пропускаем')
        continue
    elif random_number % 7 == 0:
        print(f'{random_number} остановка!')
        break
    else:
        print(random_number)
