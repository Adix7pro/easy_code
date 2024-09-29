<<<<<<< HEAD
from tkinter import *

def display():
    if(x.get()==1):
        print("you have money")
    else:
        print("you don't have money")


#python_photo = PhotoImage(file="logo.png")
window = Tk()
x = IntVar() #BOOLEANVAR()
check_button = Checkbutton(window,
                           text="i have money",
                           variable=x,
                           onvalue=1,#TRUE
                           offvalue=0,#FALSE
                           command=display,
                           font=('Arial',20),
                           fg="#00FF00",
                           bg="black",
                           activebackground="#00FF00",
                           activeforeground="black",
                           padx=25,
                           pady=10
#                           image=python_photo,
#                           compound="left"
)
check_button.pack()

window.mainloop()
=======
from tkinter import *

def display():
    if(x.get()==1):
        print("you have money")
    else:
        print("you don't have money")


#python_photo = PhotoImage(file="logo.png")
window = Tk()
x = IntVar() #BOOLEANVAR()
check_button = Checkbutton(window,
                           text="i have money",
                           variable=x,
                           onvalue=1,#TRUE
                           offvalue=0,#FALSE
                           command=display,
                           font=('Arial',20),
                           fg="#00FF00",
                           bg="black",
                           activebackground="#00FF00",
                           activeforeground="black",
                           padx=25,
                           pady=10
#                           image=python_photo,
#                           compound="left"
)
check_button.pack()

window.mainloop()
>>>>>>> bf5130f4acf23800adc5c6fbb8d5c9006e134dd9
