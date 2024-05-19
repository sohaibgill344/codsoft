#contact_book
import tkinter as tk
from tkinter import messagebox, simpledialog


contacts = []

def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    
    if name and phone:
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        update_contact_list()
    else:
        messagebox.showerror("Input Error", "Name and phone number are required.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def view_contact():
    selected = contact_list.curselection()
    if selected:
        contact = contacts[selected[0]]
        details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
        messagebox.showinfo("Contact Details", details)
    else:
        messagebox.showerror("Selection Error", "No contact selected.")

def search_contact():
    query = simpledialog.askstring("Input", "Enter name or phone number to search:")
    if query:
        found_contacts = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
        if found_contacts:
            result = "\n".join([f"{c['name']} - {c['phone']}" for c in found_contacts])
            messagebox.showinfo("Search Results", result)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")
    else:
        messagebox.showerror("Input Error", "Please enter a search query.")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        contact = contacts[selected[0]]
        name = simpledialog.askstring("Input", "Enter name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Input", "Enter phone number:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Input", "Enter email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Input", "Enter address:", initialvalue=contact['address'])
        
        if name and phone:
            contacts[selected[0]] = {"name": name, "phone": phone, "email": email, "address": address}
            update_contact_list()
        else:
            messagebox.showerror("Input Error", "Name and phone number are required.")
    else:
        messagebox.showerror("Selection Error", "No contact selected.")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        del contacts[selected[0]]
        update_contact_list()
    else:
        messagebox.showerror("Selection Error", "No contact selected.")

root = tk.Tk()
root.title("Contact Book")

contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(button_frame, text="View Contact", command=view_contact)
view_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.grid(row=0, column=2, padx=10)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=0, column=3, padx=10)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=4, padx=10)

root.mainloop()
