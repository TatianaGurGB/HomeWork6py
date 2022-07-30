# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = (input('Введите вещественное число '))
sum = 0
# for el in num:
#     if el != '.':
#         el = int(el)
#         sum += el
#     else:
#         pass
# print(sum)

f = [int(el) for el in num if (el != '.')]
for el in f:
    sum += el
print(sum)