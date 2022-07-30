# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

# первоначальное решение:
# n = int(input('Введите число '))
# my_list = []

# for i in range(-n, n + 1):
#     my_list.append(i)

# print(my_list)
# posit1 = int(input('Введите значение позиции 1: '))
# posit2 = int(input('Введите значение позиции 2: '))
# multiplication = my_list[posit1] * my_list[posit2]
# print(multiplication)


n = int(input('Введите число '))
my_list = []

my_list =[i for i in range(-n, n + 1)]   #включение
print(my_list)

posit1 = int(input('Введите значение позиции 1: '))
posit2 = int(input('Введите значение позиции 2: '))
multiplication = my_list[posit1] * my_list[posit2]
print(multiplication)