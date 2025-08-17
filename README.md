# Contact Management System (Tkinter)

A simple **Contact Management System** built with **Python (Tkinter)**.  
This app allows users to **add, update, delete, and view contacts**. Contacts are stored in a `contacts.json` file for persistence.

---

## Features

- Add new contacts (Name, Phone, Email)
- Edit/update existing contacts
- Delete contacts
- View all contacts in a list
- Persistent storage using `contacts.json`

---

## Tech Stack

- **Python 3.x**
- **Tkinter** (built-in GUI library in Python)
- **JSON** for storage
  Project Structure
  contact-app/
  │── contact_app.py # Main application
  │── contacts.json # Data file (auto-created after running app)
  │── README.md # Project documentation
  │── .gitignore # Git ignore rules

> > How to Run

> > Clone this repository:

git clone https://github.com/your-username/contact-app.git
cd contact-app

> > Run the application:

python contact_app.py

The GUI window will open. You can now add, edit, delete, and view contacts.

> > Requirements
> > Python 3.x
> > Tkinter (comes pre-installed with Python)
> > Notes
> > Contacts are stored in a contacts.json file in the project directory.

To reset, delete the contacts.json file.

Add contacts.json to .gitignore if you don’t want to upload saved contacts.
