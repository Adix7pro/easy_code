<<<<<<< HEAD
from tkinter import *
def submit():
    username = entry.get()
    print("Hi ", username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

 

window = Tk()
entry = Entry(window,
              font=("Arial",50),
                fg="#00FF00",
                bg="black",
                show = "*")
entry.pack(side = LEFT)


submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
delete_button = Button(window,text="delete",command= delete)
delete_button.pack(side=RIGHT)
backspace_button = Button(window,text="backspace",command = backspace)
backspace_button.pack(side=RIGHT)
=======
from tkinter import *
def submit():
    username = entry.get()
    print("Hi ", username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

 

window = Tk()
entry = Entry(window,
              font=("Arial",50),
                fg="#00FF00",
                bg="black",
                show = "*")
entry.pack(side = LEFT)


submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
delete_button = Button(window,text="delete",command= delete)
delete_button.pack(side=RIGHT)
backspace_button = Button(window,text="backspace",command = backspace)
backspace_button.pack(side=RIGHT)
>>>>>>> bf5130f4acf23800adc5c6fbb8d5c9006e134dd9
window.mainloop()