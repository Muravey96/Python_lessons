""" За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input: n = 700  m = 750   Output:2 """ 

n = int(input("Машина за день проезжает:"))
m = int(input("Длинна маршрута:"))
print(-(-m//n))

""" Вариант посложненее с округлеием до большего
n = int(input("Машина за день проезжает:"))
m = int(input("Длинна маршрута:"))
d = math.ceil(m/n)
print(f'Количество дней {m} - {d}) """



