# 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!

# ("poly.txt", 'r') as data1, open("poly_2.txt", 'r') as data2,

data1 = open('poly.txt').read().split('\n')
data2 = open('poly_2.txt').read().split('\n')
if len(data1) != len(data2):
        print("Количество строк не совпадает")   
else: 
    with open ("poly.txt", 'r') as data1, open("poly_2.txt", 'r') as data2, open ("sum_poly.txt", "w+") as result:
        for line1, line2 in zip(data1, data2): 
            result.write(line1.replace('= 0', '+ ').rstrip('\n') + line2)