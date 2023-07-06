import tkinter as tk

class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

def character_sheet():
    form = tk.Tk()
    form.geometry('500x500')
    form.title("Character Sheet")
    
    core_heading = tk.Label(form, text="Core", width=20,font=("bold",20))
    core_heading.place(x=0, y=10)
    name_label = tk.Label(form, text="Name",width=20,font=(14))
    name_label.place(x=-80,y=40)
    name_entry = tk.Entry(form)
    name_entry.place(x=0, y=65)
    level_label = tk.Label(form, text="Level", width=20,font=(14))
    level_label.place(x=-80,y=80)
    level_entry = tk.Entry(form)
    level_entry.place(x=0, y=105)
    
    race_label = tk.Label(form, text="Race", width=20,font=(14))
    race_label.place(x=60,y=40)
    race_entry = tk.Entry(form)
    race_entry.place(x=150, y=65)
    background_label = tk.Label(form, text="Background", width=20,font=(14))
    background_label.place(x=88,y=80)
    background_entry = tk.Entry(form)
    background_entry.place(x=150,y=105)
    #If I can find a way to show relevant information, might make these two a dropdown or some other sort of graphical menu

    #todo: Function to work out what stats should be based on Race+Background+Dice Rolls


    def submit():
        name = name_entry.get()
        filename = name + ".ddchar"
        level = level_entry.get()
        race = race_entry.get()
        background = background_entry.get()
        with open(filename, 'w') as file:
            file.write(name + "\n")
            file.write(level + "\n")
            file.write(race + "\n")
            file.write(background + "\n")
            file.write("TBA" + "\n")
            file.write("TBA" + "\n")
            file.write("TBA" + "\n")
            file.write("TBA" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")
            file.write("1" + "\n")

    submit_btn = tk.Button(form, text="Submit", command=submit)
    submit_btn.pack()