from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Helvetica", 10)
BACKGROUND = "#FEFBF6"
SEARCH_COLOR = "#35A29F"
GENERATE_PASSWORD_COLOR = "#0B666A"
ACTIVE_BG_COLOR = "#97FEED"
ADD_COLOR = "#071952"
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                 json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)     
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)     

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(height=200, width=200, bg=BACKGROUND, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

#Labels
website_label = Label(text="Website:  ", font=FONT, bg=BACKGROUND)
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text="Username:  ", font=FONT, bg=BACKGROUND)
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:  ", font=FONT, bg=BACKGROUND)
password_label.grid(row=3, column=0, pady=5)

#Entries
website_entry = Entry(width=27, font=FONT)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()

email_entry = Entry(width=45, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "pragyan@gmail.com")

password_entry = Entry(width=27, font=FONT)
password_entry.grid(row=3, column=1, pady=5)

#Buttons
search_button = Button(text="Search", width=14, command=find_password, fg="white", bg=SEARCH_COLOR, activebackground=ACTIVE_BG_COLOR, activeforeground="white", relief="raised", font=FONT, highlightthickness=0)
search_button.grid(row=1, column=2, pady=5)
generate_password_button = Button(text="Generate Password", command=generate_password, fg="white", bg=GENERATE_PASSWORD_COLOR, activebackground=ACTIVE_BG_COLOR, activeforeground="white", relief="raised", font=FONT, highlightthickness=0)
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=39, command=save, fg = "white", bg=ADD_COLOR, activebackground=ACTIVE_BG_COLOR, font=FONT, relief="raised", highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
