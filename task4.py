# 4.* Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (от 0 до 10) многочлена, записать в файл полученный 
# многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
from random import randint, choice
k1 = int(input("Задайте натуральную степень: "))

def polynomial(k):
    if k <= 0:
        print("Введено некорректное значение")
    else:
        with open("dz4.txt", "a", encoding="utf-8") as dz4:
            y = ""
            while k > 0:
                idx = randint(0,4)
                sign = ['+', '-']
                s = choice(sign)
                if idx == 0:
                    k -= 1
                else:
                    y += (f"{idx}*x^{k} {s} ")
                    k -= 1
            dz4.write(f"{y}{idx+1} = 0\n")
                    
polynomial(k1)
