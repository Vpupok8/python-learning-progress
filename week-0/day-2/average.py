# Функция расчёта средней арифметической: Напиши функцию average(numbers),
# которая принимает список чисел и возвращает их среднее значение.

def average(numbers):
    result = 0
    for i in numbers:
        result += i
    return result / len(numbers)
    
print(average([1,2,3]))
