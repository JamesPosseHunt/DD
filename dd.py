from random import randint
import tkinter.messagebox
from tkinter import *
import sys


def d4():
    result = randint(1, 4)
    tkinter.messagebox.showinfo("You rolled a ", result)

def d6():
    result = randint(1, 6)
    tkinter.messagebox.showinfo("You rolled a ", result)

def d8():
    result = randint(1, 8)
    tkinter.messagebox.showinfo("You rolled a ", result)

def d10():
    result = randint(1, 10)
    tkinter.messagebox.showinfo("You rolled a ", result)

def d12():
    result = randint(1, 12)
    tkinter.messagebox.showinfo("You rolled a ", result)

def d20():
    result = randint(1, 20)
    tkinter.messagebox.showinfo("You rolled a ", result)

def get_input(text_box):
    value = text_box.get("1.0", "end-1c")
    return value

def char_sheet():
    char_win = Tk()
    char_win.title("Character Sheet")
    char_text = Text(char_win, height=2, width=5)
    char_text.pack()
    enter_name = Button(char_win, text="Name", height=2, width=5)
    enter_name.pack()

def dice():
    dice_win = Tk()
    dice_win.title("Dice")
    b4 = Button(dice_win, text="D4", width=10, height=5,
                activebackground='blue', bg='grey', command=d4)
    b4.pack()
    b6 = Button(dice_win, text="D6", width=10, height=5,
                activebackground='blue', bg='grey', command=d6)
    b6.pack()
    b8 = Button(dice_win, text="D8", width=10, height=5,
                activebackground='blue', bg='grey', command=d8)
    b8.pack()
    b10 = Button(dice_win, text="D10", width=10, height=5,
                 activebackground='blue', bg='grey', command=d10)
    b10.pack()
    b12 = Button(dice_win, text="D12", width=10, height=5,
                 activebackground='blue', bg='grey', command=d12)
    b12.pack()
    b20 = Button(dice_win, text="D20", width=10, height=5,
                 activebackground='blue', bg='grey', command=d20)
    b20.pack()


root = Tk()
root.title("DD")
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=sys.exit)

dice_btn = Button(root, text="Roll Dice", width=20, height=10,
                  activebackground='blue', bg='grey', command=dice)
dice_btn.pack()

char_button = Button(root, text="Character Sheet", width=20, height=10,
                     activebackground='blue', bg='grey', command=char_sheet)
char_button.pack()

root.mainloop()
