from tkinter import *

def convert_to_km():
    miles_entered = float(input.get())
    Kilometers = miles_entered * 1.609
    km_value.config(text=f"{Kilometers}")
    
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

input = Entry()
input.grid(row=0, column=1)


label_one = Label(text="Miles")
label_one.grid(row=0, column=2)
label_one.config(padx=20, pady=20)

label_two = Label(text="is equal to")
label_two.grid(row=1, column=0)
label_two.config(padx=20, pady=20)

km_value = Label()
km_value.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="calculate", command=convert_to_km)
button.grid(row=2, column=1)


window.mainloop()