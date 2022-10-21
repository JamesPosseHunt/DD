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

def dice():
    dice_win = Tk()
    dice_win.title("Dice")

    b4 = Button(dice_win, text="D4", width=10, height=5, activebackground='blue', bg='grey', command=d4)
    b4.pack()

    b6 = Button(dice_win, text="D6", width=10, height=5, activebackground='blue', bg='grey', command=d6)
    b6.pack()

    b8 = Button(dice_win, text="D8", width=10, height=5, activebackground='blue', bg='grey', command=d8)
    b8.pack()

    b10 = Button(dice_win, text="D10", width=10, height=5, activebackground='blue', bg='grey', command=d10)
    b10.pack()

    b12 = Button(dice_win, text="D12", width=10, height=5, activebackground='blue', bg='grey', command=d12)
    b12.pack()

    b20 = Button(dice_win, text="D20", width=10, height=5, activebackground='blue', bg='grey', command=d20)
    b20.pack()

root = Tk()
root.title("DD")
#root.iconbitmap('assets/dd.ico')

dice_btn = Button(root, text="Dice", width=10, height=5, activebackground='blue', bg='grey', command=dice)
dice_btn.pack()

root.mainloop()
