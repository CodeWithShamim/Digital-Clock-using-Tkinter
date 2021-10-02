from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
s = root.title("Digital Clock(@shamim)")

def clock():
    tick = strftime('%H:%M:%S %p %a')
    label.config(text=tick)
    label.after(1000, clock)

label = Label(root, font=('sans', 100), background='black', foreground='red')
label.pack(anchor='center')

clock()
mainloop()