""" У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.
 ПРИМЕР: 
 Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print(‘ok’)
else:
 print(‘fail’)
Вывод:
ok"""

values = [1, 23, 42, 'asdfg']
transformation = lambda x: x
transformed_values = list(map(transformation, values)) # list - применяем, тк map - вернет тип данных, с которым мы не сможем взаимодействовать
if values == transformed_values:
    print('ok')
else:
    print('fail')

# map(transformation, values - эта фраза означает, что map применяет заложенную в transformation функцию (lambda x: x) 
# к каждому элементу списка values, в итоге тк x: x, то она и ничего не меняет.

# !! В данном случае мы как бы перенесли значения из списка values в другой список, при этом мы не 
# создали "конект" между списками, мы можем отдельно работать с каждым списком не влияя на другой.
# Если просто написать values = transformd_values, то при изменении одного списка, другой тоже будет меняться. 
# Для копирования значения можно использовать ф-ю .copy() 