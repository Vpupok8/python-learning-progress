# Функция расчёта средней арифметической: Напиши функцию average(numbers),
# которая принимает список чисел и возвращает их среднее значение.

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
    
print(average([1,2,3]))
