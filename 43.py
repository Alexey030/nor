import random
a = [random.randrange(-1000, 1000) for i in range(10)]
print(a)
g = max(a)
print("максимальное число: ", g)
f = min(a)
print("минимальное число: ", f)
print("кол-во + чисел:", sum(i > 0 for i in a))#сумма положительных чисел
print("кол-во - чисел:", sum(i < 0 for i in a))#сумма отрицательных числе 
print("кол-во 0 чисел:", sum(i == 0 for i in a))#Количество нулей