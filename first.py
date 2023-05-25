#Драгунова Анастасия Евгеньевна Группа 44-22-115 Вариант 6 Задание 1
import math
import numpy as np
def calculate(number):
    temp = []
    for n in number:
        temp.append(func(n))
        #print('x: ',n)
        #print('Результат: ',temp)
    return temp   
        
        
def func(x):
    if(x<0.5):
        temp=float(x*np.arctan(x))
        return temp
    else:
        temp=float(np.sin(1/x))
        return temp
print("Сколько чисел считать ?")
while True:
    try:
        inp = int(input())
    except ValueError:
        print('Введите число')
    else:
        break
number = []
final = [] 
while(inp!=0):
    print('Введите число')
    try:
        temp = float(input())
    except ValueError:
        print('Введите число')
    else:
        number.append(temp)
        inp-=1
final.append(calculate(number))
print('x: ',number)
print('Результат: ',final)
