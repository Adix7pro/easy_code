<<<<<<< HEAD
from tkinter import *
window = Tk()
foods = ["pizza","hamburger","hotdog"]

def order():
    if(f.get()==0):
        print("You ordered pizza !")
    elif(f.get()==1):
        print("You ordered hamburger !")
    elif(f.get()==2):
        print("You ordered hotdog !")
    else:
        print("wrong ! try again")
pizzaImage = PhotoImage(file="photo_png//Photos.png")
hamburgerImage = PhotoImage(file="photo_png//Photos.png")
hotdogImage = PhotoImage(file="photo_png//Photos.png")
foodsImages = [pizzaImage,hamburgerImage,hotdogImage]

f = IntVar()
for food in range(len(foods)):
    radiobutton = Radiobutton(window,
                              text=foods[food],
                              variable = f,
                              value = food,
                              padx = 25,
                              font = ('Impact',50),
                              image = foodsImages[food],
                              compound = "left",
                              indicatoron = 0,
                              width = 500,
                              command = order)
    # radiobutton.config()
    radiobutton.pack(anchor=W)
window.mainloop()
=======
from tkinter import *
window = Tk()
foods = ["pizza","hamburger","hotdog"]

def order():
    if(f.get()==0):
        print("You ordered pizza !")
    elif(f.get()==1):
        print("You ordered hamburger !")
    elif(f.get()==2):
        print("You ordered hotdog !")
    else:
        print("wrong ! try again")
pizzaImage = PhotoImage(file="photo_png//Photos.png")
hamburgerImage = PhotoImage(file="photo_png//Photos.png")
hotdogImage = PhotoImage(file="photo_png//Photos.png")
foodsImages = [pizzaImage,hamburgerImage,hotdogImage]

f = IntVar()
for food in range(len(foods)):
    radiobutton = Radiobutton(window,
                              text=foods[food],
                              variable = f,
                              value = food,
                              padx = 25,
                              font = ('Impact',50),
                              image = foodsImages[food],
                              compound = "left",
                              indicatoron = 0,
                              width = 500,
                              command = order)
    # radiobutton.config()
    radiobutton.pack(anchor=W)
window.mainloop()
>>>>>>> bf5130f4acf23800adc5c6fbb8d5c9006e134dd9
