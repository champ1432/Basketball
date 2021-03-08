from tkinter import *
from tkinter import messagebox
from Sim import commentary, home_starting, away_starting

# define window size, title, and background color
win = Tk()
win.title("Sim Window")
win.config(bg="#787878")

# defines buttons and Labels
open_comm = Label(win, text=commentary(), wraplength=275, bg="#787878").grid(row=0, column=2)
hsl = Label(win, text=home_starting(), bg="#787878").grid(row=1, column=1)
asl = Label(win, text=away_starting(), bg="#787878").grid(row=1, column=3)
win.mainloop()
