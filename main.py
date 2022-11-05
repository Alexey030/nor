a=int(input("Введите длинну: "))
b=int(input("Введите ширину: "))
j=input("Введите символ: ")
print(j*a)
for i in range(b-2):print(j," "*(a-2),j,sep="")#*a-2 для того чтобы получить пустоту внутри прямоугольника
print(j*a)