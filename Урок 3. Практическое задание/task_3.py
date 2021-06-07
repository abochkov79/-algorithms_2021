﻿"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

my_set1 = set()
my_set2 = set()

s = "papa"
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j + 1] != s:
            my_set1.add(hash(s[i:j + 1]))
            my_set2.add(s[i:j + 1])

print("Первоначальная строка:", s)
print("Количество уникальных подстрок:", len(my_set1))
for i in my_set2:
    print(i)
