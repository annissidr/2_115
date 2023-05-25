#Драгунова Анастасия Евгеньевна Группа 44-22-115 Вариант 6 Задание 3
import tkinter
import numpy as np
def func():
    x=float(entry_x.get())
    if(x<0.5):
        temp=float(x*np.arctan(x))
        
    else:
        temp=float(np.sin(1/x))
    result.config(text=temp)    

root=tkinter.Tk()
root.title("third")
input_x=tkinter.Label(root, text=" Введи x")
input_x.grid(row=0, column=0)
entry_x=tkinter.Entry(root)
entry_x.grid(row=0, column=1)
button=tkinter.Button(root, text="Подсчет", command=func)
button.grid(row=1, column=0)
result=tkinter.Label(root, text="")
result.grid(row=1, column=1)
root.mainloop()