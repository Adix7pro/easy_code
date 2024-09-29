from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    # if messagebox.askokcancel(title="ask ok cancel",message="Do you want to do the thing?"):
    #     print("you did a thing!")
    # else:
    #     print("You canceled a thing: :(")
        
    # if messagebox.askretrycancel(title="ask ok cancel",message="Do you want retry the thing?"):
    #     print("you retried a thing!")
    # else:
    #     print("You canceled a thing: :(")
    # if messagebox.askyesno(title='ask yes or no',message='do you like cake'):
    #     print('I like cake too :)')
    # else:
    #     print('i do not like it :(')
    
    # answer = messagebox.askquestion(title="ask question",message='do you like pie ?')
    # if (answer == 'yes'):
    #     print('i like pie too')
    # else:
    #     print('why do you not like pie? :(') 
    

    answer = messagebox.askyesnocancel(title="YES NO CANCEL",message='do you like to CODING ?',icon='info')
    if (answer == True):
        print('GOOD LUCK !!!')
    elif (answer == False):
        print('why do you not like TO CODING? :(') 
    else:
        print('you have a dodged  the question')
        
    
    
#    messagebox.showerror(title="ERROR",message="something went wrong :(")
#while(True):
#    messagebox.showwarning(title="WARNING",message="You have a VIRUS !!!")
    
#    messagebox.showinfo(title="Attention",message="You are a person")

button = Button(window,
                command=click,
                text="click me")
button.pack()
window.mainloop()