# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Введите число: '))

def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
list = []
for i in range (1, n):              # list = [i for i in range (1, n)]  включение
    list.append(fibo(i))
print(list)