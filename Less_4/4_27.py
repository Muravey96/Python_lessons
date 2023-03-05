""" Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13  """

words = set(input().lower().split()) # set - создание множества уникальных объектов, тоесть он впишет все слова по 1му экземпляру
# lower - снижаем регистр, чтобы было одинаково,  split - убираем лишние пробелы, чтобы считалось как отдельные элементы
print(len(words)) # len - подсчет длинны (кол-ва слов)