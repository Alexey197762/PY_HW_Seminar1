#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

print("Введите цифру, обозначающую день недели:")
day = int(input())

if ( 0 < day < 6):
    print("Этот день не выходной")
elif (day == 6 or day == 7):
    print("Это выходной !!!")
else:
    print("Ошибка! Число не входит в промежуток от 1 до 7")