import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "contacts.json"

# ---------------- Data Handling ---------------- #
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

# ---------------- App Class ---------------- #
class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("500x400")

        self.contacts = load_contacts()

        # Input fields
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, pady=5)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Update Contact", command=self.update_contact).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).grid(row=3, column=2, pady=10)

        # Contact List
        self.listbox = tk.Listbox(root, width=60, height=12)
        self.listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.load_selected_contact)

        # Load existing contacts
        self.refresh_list()

    # -------- Functions -------- #
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, c in enumerate(self.contacts):
            self.listbox.insert(tk.END, f"{idx+1}. {c['name']} - {c['phone']} - {c['email']}")

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts(self.contacts)
        self.refresh_list()
        self.clear_entries()

    def load_selected_contact(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        contact = self.contacts[index]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact["name"])
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact["phone"])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact["email"])

    def update_contact(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a contact to update.")
            return
        index = selection[0]
        self.contacts[index] = {
            "name": self.name_entry.get().strip(),
            "phone": self.phone_entry.get().strip(),
            "email": self.email_entry.get().strip(),
        }
        save_contacts(self.contacts)
        self.refresh_list()
        self.clear_entries()

    def delete_contact(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a contact to delete.")
            return
        index = selection[0]
        confirm = messagebox.askyesno("Confirm", "Delete this contact?")
        if confirm:
            del self.contacts[index]
            save_contacts(self.contacts)
            self.refresh_list()
            self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


# ---------------- Run App ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
