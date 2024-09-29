from tkinter import *#mashina tezligini qilish
def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")
window = Tk()
hotImage = PhotoImage(file = "photo_png//logo.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()
scale = Scale(window,
              from_ = 100,
              to=0,
              length=600,
              orient= VERTICAL,#HORIZONTAL,#orientation
              font = ('Consolas',20),
              tickinterval = 10,
#              showvalue= 0
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg = '#111111')
scale.set(((scale["from"]-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file = "photo_png//click.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()

window.mainloop()