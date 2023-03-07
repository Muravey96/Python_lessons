""" Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается  объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3 """

def rev_num(num):
    if num == 0:
        return " "
    nums = input()
    return rev_num(num - 1) + f"{nums} "


print(rev_num(int(input())))

# ------------------------------

# n = input()
# nums = input()
# print(nums[::-1]) - это вариант среза

# А еще есть .reverse :
# my_list = [1, 'two', 'a', 4]
# my_list.reverse()  # None
# my_list  # [4, 'a', 'two', 1]