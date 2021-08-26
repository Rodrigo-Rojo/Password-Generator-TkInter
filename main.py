from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def create_random_pass():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    user = username_input.get()
    user_pass = password_input.get()
    if len(website) == 0 or len(user_pass) == 0:
        messagebox.showerror(title="Opps", message="Please don't leave any fields empty")
    elif messagebox.askokcancel(title=website, message=f"Is your data correct?"):
        data = open("password_data.txt", mode="a")
        data.write(f"{website} | {user} | {user_pass}\n")
        data.close()
        website_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo(title=website, message="Your password has been saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", font=("Courier", 11, "bold"))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Courier", 11, "bold"))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Courier", 11, "bold"))
password_label.grid(column=0, row=3)

# Inputs

website_input = Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "sori_awp_@live.com")

password_input = Entry(width=34)
password_input.grid(column=1, row=3)

#  Buttons

password_button = Button(text="Generate Password", command=create_random_pass)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_data, width=44)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
