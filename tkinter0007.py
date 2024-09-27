from tkinter import *

window = Tk()

photo = PhotoImage(file="logo.png")
label = Label(window,
              text = "Hello World, i don't remember elif",
              font=('Arial',40,'bold'),
              fg="#262ceb",
              bg="#050505",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound ="bottom"#rasm pastda korinadi . "top"rasm sor=zdan yuqorida chiqadi
              )
label.pack()
#label.place(x=100,y=100)
window.mainloop()