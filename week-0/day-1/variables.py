# Задание: Работа с переменными и типами данных
# 1. Создайте переменные разных типов:
#    - строка (string)
#    - целое число (integer)
#    - число с плавающей точкой (float)
#    - булево значение (boolean)
# 2. Выведите значение каждой переменной
# 3. Выведите тип каждой переменной (используйте функцию type())
# 4. Попробуйте создать простые математические выражения (+, -, *, /)

# Ваш код здесь:
string = "Строка"
number = 35
fraction = 9.99
is_true = False

print(f'{string} {number} {fraction} {is_true}')
print(f'{type(string)} {type(number)} {type(fraction)} {type(is_true)}')
print(f'{string * 3} {number + fraction} {number - fraction} {number * fraction} {number / fraction}')
