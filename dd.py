from random import randint
import tkinter.messagebox
from tkinter import *

def d4():
    result = randint(1, 4)
    tkinter.messagebox.showinfo("Dice Roll", result)

def d6():
    result = randint(1, 6)
    tkinter.messagebox.showinfo("Dice Roll", result)

def d8():
    result = randint(1, 8)
    tkinter.messagebox.showinfo("Dice Roll", result)

def d10():
    result = randint(1, 10)
    tkinter.messagebox.showinfo("Dice Roll", result)

def d12():
    result = randint(1, 12)
    tkinter.messagebox.showinfo("Dice Roll", result)

def d20():
    result = randint(1, 20)
    tkinter.messagebox.showinfo("Dice Roll", result)

def menu():
    print("Choose Dice to Roll: ")
    print("D4 (Press 4), D6 (Press 6), D8 (Press 8)")
    print("D10 (Press 10), D12 (Press 12), D20 (Press 20)")
    print("Exit (Press 0)")

window = Tk()
window.title("DD")
window.geometry('1920x1080')

b4 = Button(window, text="D4", width=5, height=10, activebackground='blue', bg='grey', command=d4)
b4.place(x=200,y=30)

b6 = Button(window, text="D6", width=5, height=10, activebackground='blue', bg='grey', command=d6)
b6.place(x=250,y=30)

b8 = Button(window, text="D8", width=5, height=10, activebackground='blue', bg='grey', command=d8)
b8.place(x=300, y=30)

b10 = Button(window, text="D10", width=5, height=10, activebackground='blue', bg='grey', command=d10)
b10.place(x=350, y=30)

b12 = Button(window, text="D12", width=5, height=10, activebackground='blue', bg='grey', command=d12)
b12.place(x=400, y=30)

b20 = Button(window, text="D20", width=5, height=10, activebackground='blue', bg='grey', command=d20)
b20.place(x=450, y=30)

window.mainloop()
