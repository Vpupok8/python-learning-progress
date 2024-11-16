# Функция перевода градусов: Напиши функцию convert_temperature(celsius),
# которая переводит температуру из градусов Цельсия в Фаренгейты

def convert_temperature(celsius):
    return celsius * 9 / 5 + 32

celsius = float(input("Введите значение цельсия: "))

print(f'{celsius} по Цельсию, равняется {convert_temperature(celsius):.2f} по Фаренгейту ')
