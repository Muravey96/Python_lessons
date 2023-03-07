"""Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
# VAR 1 -------------------------------------

num = int(input())
grades = list(map(int, input().split())) # map - Применяет указанную функцию к каждому элементу указанной последовательности
num_max = max(grades)
num_min = min(grades)

grades_change = [num_min if j == num_max else j for j in grades]
print(grades_change)


# VAR 2 -------------------------------------

from random import randint
# Можно сделать import random
# Тогда дальше надо прописывать array = [random.randint(1, 5) for i in range(n)]

n = int(input('Введите кол-во оценок: '))
array = [randint(1, 5) for i in range(n)]
print(array)

num_max = max(array)
num_min = min(array) 

num = [num_min if i == num_max else i for i in array ] 
                        # for i in array - смотрим конкретное значение в конкретном списке
                        # num_min if i == num_max - если значение num_min равно максимальному, то мы переписываем его в минимальный, 
                        # else i - если нет, то ничего не меняем, оставляем этоже значение
print(num)



