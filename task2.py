# 2. Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

def is_num_prime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range (3, int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True

def create_prime_factor_list(num1):
    factor = 2
    res_list = []
    while num1 > 1:
        if num1 % factor == 0 and is_num_prime(factor):
            res_list.append(factor)
            num1 = num1 / factor
        else:
            factor += 1
    return res_list

number = int(input("Введите натуральное число: "))
print(create_prime_factor_list(number))