
from os import path

file_base = "base.txt" # Задаем название файлу, вкладываем его в переменную
last_id = 0
all_data = [] # пустой список

# проверка файла на существование
if not path.exists(file_base): # если в папке нет файла - 
    with open(file_base, "w", encoding="utf-8") as _: # функция переходит в режим "w", который автоматически создает файл
        pass 



# Считывание данных -------------------------
def read_records(): 
    global last_id, all_data # чтобы эти данные было видно во всех функциях и файлах.
    with open(file_base, encoding="utf-8") as f: # "utf-8" - кодировка
        all_data = [i.strip() for i in f]  # strip - очищает пробелы, i - это строка (у нас список строк)
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return [] # в случае если файл пустой, он просто вернут пустой файл. если этой строчки не будет, то при обработке пустого файла будет вылетать ошибка

# Вывод данных ----------------
def show_all(): 
    if all_data:
        print(*all_data, sep="\n") # если что-то лежит он покажет, иначе ... 
    else:
        print("Empty data")


# Добавление новых данных ------------------
def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"] 
    string = ""
    for i in array: # проходится по заданному списку, для вывода его на экран поочередно
        string += input(f"Enter {i} ") + " " # На консоль выведется Enter и элемент из списка (что надо ввести) и введенные данные запишуться в переменную стринг
    last_id += 1 # с каждым вводом счетчик увеличиться. 

    with open(file_base, "a", encoding="utf-8") as f: #  "a" - дозапись файла
        f.write(f"{last_id} {string}\n") # Выведет записанные ранее данные в last_id


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"    # то что увидит пользователь, для выбора действия
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")
main_menu()