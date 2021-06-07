﻿"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


def min_el1(lst_obj):                                # O(n^2)
    min_e = lst_obj[0]                               # O(1)
    for i in range(len(lst_obj)):                    # O(n^2)
        min_e = lst_obj[i]                           # O(1)
        for j in range(len(lst_obj)):                # O(n)
        if (i != j) and (lst_obj[j] < lst_obj[i]):   # O(1)
            min_e = lst_obj[j]                       # O(1)
    return min_e				     # O(1)


def min_el2(lst_obj):   # O(n)
    min_e = lst_obj[0]  # O(1)
    for el in lst_obj:  # O(n)
        if el < min_e:  # O(1)
            min_e = el  # O(1)
    return min_e        # O(1)

my_list = [4, 0, 1000, -4, 53215, 1,-4000]
print(min_el1(my_list))
print(min_el2(my_list))
