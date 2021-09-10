import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    if len(password_input.get()) != 0:
        password_input.delete(0, tk.END)
    password_input.insert(tk.END, string=password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="Please, fill all the fields!")
    else:
        is_ok = messagebox.askokcancel(title="Save to a file?",
                                       message=f"These are the details entered: \n"
                                               f"Website: {website}\n"
                                               f"Email: {email} \n"
                                               f"Password: {password} \n"
                                               f"Is it ok to save?"
                                       )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
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
email_input.insert(tk.END, string="user@example.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = tk.Entry(width=18)
password_input.insert(tk.END, string="")
password_input.grid(column=1, row=3)

add_button = tk.Button(text="Add", width=34, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=2, row=3)

window.mainloop()
