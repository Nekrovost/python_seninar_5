# def fib(n):
#     if n==0 or n==1:
#         return 1
#     return fib(n-1)+fib(n-2)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. (1-5)
# import random

# size=int(input('Введите кол-во оценок: '))
# list_1=[]
# min=int(input('Введите саммый выскойи бал, который можно получить: '))
# max=int(input('Введите саммый низкий бал, который можно получить: '))
# for i in range(size):
#     list_1.append(random.randint(max, min))
# print(list_1)
# for j in  range(size):
#     if list_1[j]>max:
#         max=list_1[j]
#     if list_1[j]<min:
#         min=list_1[j]
# print(min, max)
# for k in range(size):
#     if list_1[k]==max:
#         list_1[k]=min
# print(list_1)



# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# num=int(input('Введите число для проверки: '))
# count_1=0
# count_2=2
# for i in range(1,num+1):
#     if num%i==0:
#         count_1=count_1+1
# if count_1==count_2 or num==1:
#     print(f'число {num} простое')
# else:
#     print(f'число {num} не простое')


# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# import random

# N=int(input('Введите длину последовательности: '))
# list_1=[random.randint(1,9) for i in range(N)]
# print(list_1)
# count_1=0
# count_2=1
# for i in range(N//2):
#     count_1=list_1[i]
#     list_1[i]=list_1[N-count_2]
#     list_1[N-count_2]=count_1
#     count_2+=1
# print(list_1)

# Ля, надо было решить это рекурсией...


# def Revers(s):
#     return('1' if s==1 else f'{s} {Revers(s-1)}')
# num=int(input('Введите n: '))
# print(Revers(num))



# HOMEWORK

# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# def stepen(num_1,  num_2):
#     if num_2==1:
#         return num_1
#     else: 
#         return num_1*stepen(num_1, num_2-1)
# n1=int(input('Введите основание: '))
# n2=int(input('Введите степень: '))
# print(stepen(n1,n2))




# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# ЗАДАНИЕ СОВЕРШЕННО НЕКОРРЕКТНО СФОРМУЛИРОВАНО, ТОМУ КТО СОСТАВЛЯЛ ТЗ БЫЛО БЫ НЕПЛОХО НАУЧИТЬСЯ ДУМАТЬ
def summa(num_1, num_2):
    if num_1== 0:
        return num_2
    return summa(num_1-1, num_2+1)
n1=int(input('Введите первое число: '))
n2=int(input('Введите второе число: '))
print(summa(n1, n2))