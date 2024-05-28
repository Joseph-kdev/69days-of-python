from tkinter import *

def button_clicked():
    my_label.config(text=input.get())
    
    
window = Tk()
window.title("My First GUI app")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text="I am a label", font=("ariel", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


button =  Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_two =  Button(text="Click")
button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()