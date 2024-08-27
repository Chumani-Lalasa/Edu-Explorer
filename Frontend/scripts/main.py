import tkinter as tk
from tkinter import messagebox
import requests

# Create the main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")

# Create a label for the login screen
login_label = tk.Label(root, text="Login", font=("Helvetica", 16))
login_label.pack(pady=10)

# Create a label and entry for the username
username_label = tk.Label(root, text="Username")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Create a label and entry for the password
password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Function to handle login (placeholder function)
def login():
    username = username_entry.get()
    password = password_entry.get()
    response = requests.post('http://localhost:8000/api/login', json = {'username': username, 'password' : password})

    if response.status_code == 200:
        messagebox.showinfo("Login Info", response.json()['message'])
    else:
        messagebox.showinfo("Login Info", response.json()['message'])

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()


