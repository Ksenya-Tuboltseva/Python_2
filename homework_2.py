##Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата
num = int(input("Введите число "))
num_16 = '0x{:X}'.format(num).lower()
print(num_16 == hex(num))

##Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
import fractions
import math

a = '2/3'
b = '5/7'
numeric_a = int(a.split('/')[0])
denom_a = int(a.split('/')[1])
numeric_b = int(b.split('/')[0])
denom_b = int(b.split('/')[1])

# Функция для нахождения наибольшего общего делителя (НОД)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Функция для сокращения дроби
def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Функция для сложения двух дробей
def add_fractions(num1, den1, num2, den2):
    # Приведение знаменателей к общему знаменателю
    common_denominator = den1 * den2
    new_num1 = num1 * den2
    new_num2 = num2 * den1
    
    # Сложение числителей
    result_num = new_num1 + new_num2
    
    # Сокращение результата
    result_num, common_denominator = simplify_fraction(result_num, common_denominator)
    
    return result_num, common_denominator

result_num, result_den = add_fractions(numeric_a, denom_a, numeric_b, denom_b)
print(f"Результат сложения: {result_num}/{result_den}")

def multiply_fractions(num1, den1, num2, den2):
    result_num = num1 * num2
    result_den = den1 * den2
    
    # Упрощение результата
    result_num, result_den = simplify_fraction(result_num, result_den)
    
    return result_num, result_den

result_num, result_den = multiply_fractions(numeric_a, denom_a, numeric_b, denom_b)
print(f"Результат умножения: {result_num}/{result_den}")

a_2 = fractions.Fraction(2, 3)
b_2 = fractions.Fraction(5, 7)
sum_2 = a_2 + b_2
mult_2 = a_2 * b_2

print(f'Результат сложения: {sum_2}')
print(f'Результат умножения: {mult_2}')