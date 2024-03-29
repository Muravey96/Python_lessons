""" Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                        Вывод:
values = [0, 2, 10, 6]                         same
    if same_by(lambda x: x % 2, values):
        print(‘same’)
    else:
        print(‘different’) """

values = [2, 3, 6, 4]


def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1 
# ==1 - так как если все значения будут четными (делиться на 2 без остатка), то мы выведем длинну списка до 1
# метод set - вернет либо только 1, если все значения одинаковые, либо 0 и 1, если значения равные (тк set создает уникальное множество)
# len - непосредственно измеряет длинну 
# тк все четные значения при целочисленном делении дадут 1 (map применит деление), set  все единицы объединит в одну 1цу (тк это единственное уникальное значение),
# а len это все посчитает. Соответственно если все четные, то после всех действий у нас останется только одна 1ца, условия выполниться. Если будут нечетные, то будут другие значения и будет false 

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')