# Напиши функцию factorial(n), которая принимает целое 
# число n и возвращает его факториал.
# Реализуй это двумя способами:

#    С использованием цикла.
#    С использованием рекурсии.

def recursion_factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    return recursion_factorial(n - 1) * n

def cicle_factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(recursion_factorial(5))
print(cicle_factorial(3))
