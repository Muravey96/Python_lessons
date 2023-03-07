""" Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число) и некратно двум
Input: 5
Output: yes 
"""
# https://www.delftstack.com/ru/howto/python/python-isprime/

def prime_num(num):
    if num == 2 or num == 3: return True # Потому что эти два числа автоматически простые
    if num % 2 == 0 or num < 2: return False # Избегаем четные и единицу
    for i in range(3, int(num ** 0.5) + 1, 2): # 3 - c какого числа начинаем, int(num ** 0.5) - до какого числа мы будем проверять (корень нашего числа, +1, потому что дальше проверять нет смысла), 2 - это шаг (перескакиваем через число)
        if num % i == 0: # проверка если число не простое, так как это проще, а если число не подходит под это условие, оно автоматически простое (True)
            return False
    return True


print(prime_num(int(input())))

# -------------------------------------------

k = 13
# 1 not being a prime number, is ignored
if k > 1:
    for i in range(2, int(k/2)+1):
         if (k % i) == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")

else:
    print("It is not a prime number")



