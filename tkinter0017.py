from tkinter import *
from tkinter import colorchooser

window = Tk()
def click():
    # color = colorchooser.askcolor()
    # print(color)
    # colorHex = color[1]
    # print(colorHex)
    # window.config(bg=colorHex)
    #yuqoridagi kodni qisqartmasi
    window.config(bg=colorchooser.askcolor()[1])

window.geometry('420x420')
button = Button(text='click me',command=click)
button.pack()
window.mainloop()