#password_generator 
import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def on_generate():
    try:
        name = name_entry.get()
        email = email_entry.get()
        length = int(length_entry.get())
        
        if length <= 0:
            messagebox.showerror("Input Error", "Please enter a positive value for password length.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Name: {name}\nEmail: {email}\nGenerated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid value. Please enter a numeric value for password length.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your E-mail:").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter length for your password:").grid(row=2, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

