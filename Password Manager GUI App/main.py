from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Arial", 10)
BACKGROUND = "#FFF5E1"
GENERATE_PASSWORD_COLOR = "#81A263"
ADD_COLOR = "#365E32"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n{email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(height=200, width=200, bg=BACKGROUND, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=3)

#Labels
website_label = Label(text="Website:  ", font=FONT, bg=BACKGROUND)
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text="Username:  ", font=FONT, bg=BACKGROUND)
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:  ", font=FONT, bg=BACKGROUND)
password_label.grid(row=3, column=0, pady=5)

#Entries
website_entry = Entry(width=45, font=FONT)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=45, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "pragyan@gmail.com")

password_entry = Entry(width=27, font=FONT)
password_entry.grid(row=3, column=1, pady=5)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, fg = "white", bg = GENERATE_PASSWORD_COLOR, font=FONT, highlightthickness=0)
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=39, command=save, fg = "white", bg = ADD_COLOR, font=FONT, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
