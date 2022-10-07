# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint
def create_random_list(count):
    if count <= 0:
        print("Введено некорректное значение, повторите попытку")
        return []
    ls =[]
    for i in range(count):
        ls.append(randint(0,count))
    return(ls)

def find_unique_num(ls1):
    res_list = []
    for i in range(len(ls1)):
        if ls1.count(ls1[i]) == 1:
            res_list.append(ls1[i])
    return(res_list)


num = int(input("Введите количество элементов: "))
lst = create_random_list(num)
print(lst)
print(find_unique_num(lst))