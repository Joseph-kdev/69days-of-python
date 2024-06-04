from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # new_item for item in list
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    Email = user_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(Email) == 0:
        messagebox.showinfo(title="Oops", message="You have left important fields empty")
    else:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered \n Email: {Email} \n Password: {password} \n Is it Okay to save?")
        
        if is_ok:
            file = open("stuff.txt", "a")
            file.write(f"> {website} >> {Email} >>> {password} \n")
            file.close()
            
            user_input.delete(0, END)
            user_input.insert(0, "example@email.com")
            web_input.delete(0, END)
            password_input.delete(0, END)
        


# ---------------------------- UI SETUP ------------------------------- #
Window = Tk()
Window.title("Password Manager")
Window.config(padx= 50, pady= 50)

canvas = Canvas(width=200, height=200)
my_logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image = my_logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website", pady= 5)
web_label.grid(row=1, column=0)

web_input = Entry(width= 35)
web_input.focus()
web_input.grid(row= 1, column=1, columnspan=2)

user_label = Label(text="Email/Username", pady= 5)
user_label.grid(row= 2, column= 0)

user_input = Entry(width= 35)
user_input.insert(0, "example@email.com")
user_input.grid(row= 2, column=1, columnspan=2)

password_label = Label(text="Password:", pady= 5)
password_label.grid(row= 3, column= 0)

password_input = Entry(width= 21)
password_input.grid( row= 3, column= 1)

generate_pwd = Button(text="Generate Password", pady= 5, command=generate_password)
generate_pwd.grid(row= 3, column= 2)

add_button = Button(text="Add", width= 36, pady= 5, command= save)
add_button.grid(row= 4, column= 1, columnspan= 2)

Window.mainloop()

