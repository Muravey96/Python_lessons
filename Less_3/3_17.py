''' Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6 '''

counter = int(input("Сколько элементов списка вы вводите?: "))

number = []
for i in range(counter):
    number.append(int(input('введите очередное число: ')))

print(number)
num_values = len(set(number))
print(num_values)

# ИЛИ 

list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
print(len(set(list_nums)))