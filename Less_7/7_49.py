""" Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10  """

# pi - можно не считать, тк оно у всех одинаковое и не повлияет на формулу

def find_farthest_orbit(nums_list):
    s_dict = {val[0] * val[1]: val for val in nums_list if val[0] != val[1]} # {} - это словарь
# если мы хотим наоборот чтоб кортеж был ключом, а произведение элементом:
#  s_dict = {val: val[0] * val[1] for val in nums_list if val[0] != val[1]}
    return max(s_dict.items())[1] # [1]  - вытягивает кортеж

# max - примениться какраз такик ключам
# Метод items() возвращают список кортежей dict (ключ, значение)
# в нашем словаре (стр 20) элементом будет являться кортеж (число, число), а ключом к каждому кортежу станет val[0] * val[1]
# тоесть при создании словаря мы пишем - имя переменной = {ключ: элемент}

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]

# Если хотим вводить список вручную 
orbits = [tuple(map(int, input().split())) for i in range(int(input('qnt: ')))]
# Метод tuple() преобразует список элементов в кортежи.
print(*find_farthest_orbit(orbits))
