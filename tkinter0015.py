from tkinter import *

window = Tk()
 
def submit():
    foods = []
    for food in listbox1.curselection():
        foods.insert(food,listbox1.get(food))
    
    print("You have ordered: ")
    for index in foods:
        print(index)

def add():
    listbox1.insert(listbox1.size(),entryBox.get())
    listbox1.config(height=listbox1.size())

def delete():
    for food in reversed(listbox1.curselection()):
        listbox1.delete(food)
    listbox1.config(height=listbox1.size())


listbox1 = Listbox(window,
                   bg="#00ff00",
                   font=('Constantia',35),
                   width=12,
                   selectmode=MULTIPLE)

listbox1.pack()

listbox1.insert(1,'apple')
listbox1.insert(2,'banan')
listbox1.insert(3,'pig')
listbox1.insert(4,'pie')
listbox1.insert(5,'peach')

listbox1.config(height=listbox1.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,
                      text="submit",
                      command=submit)
submitButton.pack()
addButton = Button(window,
                      text="add",
                      command=add)
addButton.pack()


deleteButton = Button(window,
                      text="delete",
                      command=delete)
deleteButton.pack()

window.mainloop()