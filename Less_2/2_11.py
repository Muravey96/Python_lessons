""" Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6  """

num = int(input("Введите число: "))
a = 0
b = 1
count = 2

while num >= b:
    if num == b: #отсекающее завершающее действие
        print(count)
        break
    a , b = b , a + b # перекладывание значений двух переменных одновременно (чтобы не вводить временную переменную)
    count += 1
else:    
    print(-1)

""" Другой вариант
number = int(input("Введите число"))
result = 1
count = 3
if number == 1:
    print("Номер будет и 2 и 3")
elif number == 0:
    print("Первый номер")
else:
    while result < number:
        count += 1
        if result == number:
            break
        result = int(round(1.68 * result, 0))
        print(result)
    print("Номер будет ", count)  """