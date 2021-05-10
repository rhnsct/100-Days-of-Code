from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    uname = uname_entry.get()
    password = password_entry.get()
    

    error_message = messagebox.showerror("Missing", "Field cannot be empty!")
    
    if len(website) == 0 or len(uname) == 0 or len(password) == 0:
        error_message
    else:
        is_ok = messagebox.askyesno("Correct?", f"""Is this information correct?
                                \nWebsite: {website}\nEmail/Username: {uname}\nPassword: {password}""")
            
        if is_ok:   
            with open("manager.txt", 'a') as pass_manager:
                pass_manager.write(f"Website: {website} |Email/Username: {uname} |Password: {password}\n")     
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", font=("Arial", 10))
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username: ", font=("Arial", 10))
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password: ", font=("Arial", 10))
password_label.grid(column=0, row=3, sticky="E")

# Buttons
add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="E")

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3, sticky="E")

# Entry 
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

uname_entry = Entry(width=52)
uname_entry.grid(column=1, row=2, columnspan=2,sticky="W")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

window.mainloop()
