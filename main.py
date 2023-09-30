import random
import tkinter as tk
from tkinter import messagebox as mb
import pathlib as path
import sys
value = 0
file = path.Path("stuff", "Dice.png")
def kick():
    block = random.randint(1, 6)
    Ilp["text"] = block
window = tk.Tk()
window.title("БРОСАЙ ИХ!!!!")
window.geometry("250x70")
window.resizable(True, False)
window.iconphoto(False, tk.PhotoImage(file=file))
window.title = "игра с костями"
Ilp = tk.Label(text=value, master=window)
Ilp.pack()
Button = tk.Button(text="бросить кубик", master=window, command=kick)
Button.pack()

quest = mb.askokcancel("Leave?", "You whant to leave?")
if quest:
    sys.exit()
window.mainloop()
