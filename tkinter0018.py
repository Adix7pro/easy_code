from tkinter import *

window = Tk()
def submit():
    input = text.get('1.0',END)
    print(input)
text = Text(window,
            bg="light yellow",
            font=('Ink Free',25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()
button = Button(window,
                text='submit',
                command=submit)
button.pack()
window.mainloop()