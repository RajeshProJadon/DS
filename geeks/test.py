import sys
import tkinter as tk


win = tk.Tk()

win.title("this is title window")
lbl = tk.Label(win, text = "Enter your application name: ").grid(column = 0, row=0)
def click():
    lname= name.get()
    print(lname)
    labl = tk.Label(win, text = lname).grid(column = 0, row = 2)
    return

name = tk.StringVar()
nameEntered = tk.Entry(win, width = 12, textvariable = name).grid(column = 0, row = 1)  
# Button widget  
button = tk.Button(win, text = "submit", command = click).grid(column = 1, row = 1)
# labl = tk.Label(win).grid(column = 0, row = 2)

win.mainloop()
