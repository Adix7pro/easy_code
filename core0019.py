import time
from tkinter import *
from time import sleep
from colorama import Fore, init # type: ignore
window = Tk()


def display():
    if(b.get()==1):
        print(Fore.GREEN + "green")
        time.sleep(5)
        print(Fore.YELLOW + "yellow")
        time.sleep(5)
        print(Fore.RED + "red")
        time.sleep(17)
    else:
        print(Fore.WHITE + "green")
    
    print("Trafic_light")

b = IntVar()
button_b = Checkbutton(window,
                        text="click on",
                        variable=b,
                        onvalue=1,#TRUE
                        offvalue=0,#FALSE
                        command=display,
                        font=('Arial',20),
                        fg="#00FF00",
                        bg="black",
                        activebackground="#00FF00",
                        activeforeground="black",
                        padx=25,
                        pady=10)

button_b.pack()
display()
window.mainloop()