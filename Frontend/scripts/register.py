# import requests
# from tkinter import *
# from tkinter import messagebox
# import ast
# from PIL import Image, ImageTk


# window = Tk()
# window.title("Register")
# window.geometry('925x500+300+200')
# window.configure(bg='#fff')
# window.resizable(False, False)

# def signup():
#     username = user.get()
#     email = email_entry.get()
#     password = code.get()
#     confirm_password = confirm_code.get()

#     if password != confirm_password:
#         messagebox.showerror("Error", "Passwords do not match")
#         return
    
#     # Data to send to the Django API
#     data = {
#         'username' : username,
#         'email' : email,
#         'password' : password
#     }

#     try:
#         response = requests.post('http://127.0.0.1:8000/api/register', data=data)

#         if response.status_code == 201:
#             messagebox.showinfo("Success", "Registration successful!")
#         elif response.status_code == 400:
#             messagebox.showerror("Error", response.json().get('message'))
#         else:
#             messagebox.showerror("Error", "Registration failed, try again!")
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"failed to connect to server: {e}")
#     # logic for the sign up
#     print("logic for signup")

# # Load and resize the image
# image = Image.open('Frontend/scripts/image-1.jpg')
# resized_image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Resize to 250x250
# img = ImageTk.PhotoImage(resized_image)
# Label(window, image=img, border=0, bg='white').place(x=50, y=90)

# frame = Frame(window, width=350, height=450, bg='#fff')
# frame.place(x=480, y=50)

# heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microscoft Yahei UI Light', 23, 'bold'))
# heading.place(x = 100, y=5)

# ##########--------------------------------Username Entry
# def on_enter(e):
#     user.delete(0, 'end')
# def on_leave(e):
#     if user.get() == '':
#         user.insert(0, 'Username')
# user = Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
# user.place(x=30, y=80)
# user.insert(0, 'Username')
# user.bind("<FocusIn>", on_enter)
# user.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# #######---------------------- Email Entry
# def on_enter(e):
#     email_entry.delete(0, 'end')
# def on_leave(e):
#     if email_entry.get() == '':
#         email_entry.insert(0, 'Email')
# email_entry = Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
# email_entry.place(x=30, y=150)
# email_entry.insert(0, 'Email')
# email_entry.bind("<FocusIn>", on_enter)
# email_entry.bind("<FocusOut>", on_leave)
# Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# #######--------------------------------Password Entry
# def on_enter(e):
#     code.delete(0, 'end')
# def on_leave(e):
#     if code.get() == '':
#         code.insert(0, 'Password')
# code = Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
# code.place(x=30, y=220)
# code.insert(0, 'Password')
# code.bind("<FocusIn>", on_enter)
# code.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# ################-------------------------Confirm Password Entry

# def on_enter(e):
#     confirm_code.delete(0, 'end')
# def on_leave(e):
#     if confirm_code.get() == '':
#         confirm_code.insert(0, 'Confirm Password')
# confirm_code = Entry(frame, width=25, fg='black', border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
# confirm_code.place(x=30, y=290)
# confirm_code.insert(0, 'Confirm Password')
# confirm_code.bind("<FocusIn>", on_enter)
# confirm_code.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=317)



# #############-----------------------Sign Up Button
# Button(frame, width=39, pady=7, text='sign up', bg='#57a1f8', fg='white', border=0,command=signup).place(x=35, y=360)

# label = Label(frame, text='I have an account', fg='black', bg = 'white', font=('Microsoft Yahei UI Light', 9))
# label.place(x=90, y=400)

# signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
# signin.place(x=200, y=400)

# window.mainloop()

import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class RegisterApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Register")
        self.window.geometry('925x500+300+200')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)

        # Load and resize the image
        self.image = Image.open('Frontend/scripts/image-1.jpg')
        self.resized_image = self.image.resize((400, 400), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.resized_image)
        Label(self.window, image=self.img, border=0, bg='white').place(x=50, y=90)

        self.frame = Frame(self.window, width=350, height=450, bg='#fff')
        self.frame.place(x=480, y=50)

        self.heading = Label(self.frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        self.setup_entries()
        self.setup_buttons()

    def setup_entries(self):
        # Username Entry
        self.user = self.create_entry(self.frame, 'Username', 30, 80)
        self.email_entry = self.create_entry(self.frame, 'Email', 30, 150)
        self.code = self.create_entry(self.frame, 'Password', 30, 220)
        self.confirm_code = self.create_entry(self.frame, 'Confirm Password', 30, 290)

    def create_entry(self, parent, placeholder, x, y):
        entry = Entry(parent, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        entry.place(x=x, y=y)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.on_entry_focus_in(entry, placeholder))
        entry.bind("<FocusOut>", lambda e: self.on_entry_focus_out(entry, placeholder))
        Frame(parent, width=295, height=2, bg='black').place(x=x-5, y=y+27)
        return entry

    def on_entry_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, 'end')

    def on_entry_focus_out(self, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)

    def setup_buttons(self):
        Button(self.frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=self.signup).place(x=35, y=360)

        label = Label(self.frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
        label.place(x=90, y=400)

        signin = Button(self.frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
        signin.place(x=200, y=400)

    def signup(self):
        username = self.user.get()
        email = self.email_entry.get()
        password = self.code.get()
        confirm_password = self.confirm_code.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        data = {
            'username': username,
            'email': email,
            'password': password
        }

        try:
            response = requests.post('http://127.0.0.1:8000/api/register', data=data)

            if response.status_code == 201:
                messagebox.showinfo("Success", "Registration successful!")
            elif response.status_code == 400:
                messagebox.showerror("Error", response.json().get('message'))
            else:
                messagebox.showerror("Error", "Registration failed, try again!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")

if __name__ == "__main__":
    root = Tk()
    app = RegisterApp(root)
    root.mainloop()

