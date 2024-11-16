# Функция расчёта простых чисел: Напиши функцию is_prime(n),
# которая проверяет, является ли число простым.
# Используй её для вывода всех простых чисел от 1 до 100.
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(1, 100):
    print(f'Число {i} - {is_prime(i)}')

