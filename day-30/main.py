import json
import secrets
import tkinter as tk
from random import shuffle
from tkinter import messagebox

from pyperclip import copy

JSON_FILE = "data.json"
DEFAULT_EMAIL = "user@example.com"


def find_password():
    website = website_input.get()
    try:
        with open(JSON_FILE, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"Info for {website}",
                message=f"Email: {email}\nPassword: {password}",
            )
        else:
            messagebox.showinfo(
                title="Info", message=f"No details for the {website} exist"
            )


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = (
        [secrets.choice(letters) for _ in range(secrets.choice(range(8, 10)))]
        + [secrets.choice(symbols) for _ in range(secrets.choice(range(2, 4)))]
        + [secrets.choice(numbers) for _ in range(secrets.choice(range(2, 4)))]
    )

    shuffle(password_list)
    password = "".join(password_list)
    if len(password_input.get()) != 0:
        password_input.delete(0, tk.END)
    password_input.insert(tk.END, string=password)
    copy(password)


def save_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="Please, fill all the fields!")
    else:
        try:
            with open(JSON_FILE, "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(JSON_FILE, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open(JSON_FILE, "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


window = tk.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = tk.Entry(width=35)
website_input.insert(tk.END, string="")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = tk.Entry(width=35)
email_input.insert(tk.END, string=DEFAULT_EMAIL)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tk.Entry(width=18)
password_input.insert(tk.END, string="")
password_input.grid(column=1, row=3)

add_button = tk.Button(text="Add", width=34, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

password_button = tk.Button(
    text="Generate Password", width=15, command=generate_password
)
password_button.grid(column=2, row=3)

search_button = tk.Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
