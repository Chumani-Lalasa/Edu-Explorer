import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")

# Create a label for the login screen
login_label = tk.Label(root, text="Login", font=("Georgia", 16))
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

# "Remember Me" checkbox
remember_me = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(root, text="Remember Me", variable=remember_me)
remember_me_checkbox.pack(pady=5)

# Function to handle login (placeholder function)
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "user" and password == "pass":  # Placeholder logic
        if remember_me.get():
            messagebox.showinfo("Login Info", "Login Successful! (Credentials saved)")
        else:
            messagebox.showinfo("Login Info", "Login Successful!")
    else:
        messagebox.showwarning("Login Info", "Invalid Credentials")
        
# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
