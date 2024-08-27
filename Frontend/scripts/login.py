# import requests
# from tkinter import *
# from tkinter import messagebox
# from tkinter import *
# from PIL import ImageTk, Image
# from signup  import RegisterApp

# class LoginPage:
#     def __init__(self, window):
#         self.window = window
#         self.window.geometry('1166x718')
#         self.window.resizable(0, 0)
#         self.window.state('zoomed')
#         self.window.title('Login Page')

#         # Background image
#         self.bg_frame = Image.open('Frontend/scripts/images/background1.png')
#         photo = ImageTk.PhotoImage(self.bg_frame)
#         self.bg_panel = Label(self.window, image=photo)
#         self.bg_panel.image = photo
#         self.bg_panel.pack(fill='both', expand='yes')

#         # Login Frame
#         self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
#         self.lgn_frame.place(x=200, y=70)

#         # Welcome Heading
#         self.txt = "WELCOME"
#         self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
#                              fg='white', bd=5, relief=FLAT)
#         self.heading.place(x=80, y=30, width=300, height=30)

#         # Left Side Image
#         self.side_image = Image.open('Frontend/scripts/images/vector.png')
#         photo = ImageTk.PhotoImage(self.side_image)
#         self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.side_image_label.image = photo
#         self.side_image_label.place(x=5, y=100)

#         # Sign In Image
#         self.sign_in_image = Image.open('Frontend/scripts/images/hyy.png')
#         photo = ImageTk.PhotoImage(self.sign_in_image)
#         self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.sign_in_image_label.image = photo
#         self.sign_in_image_label.place(x=620, y=130)

#         # Sign In Label
#         self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
#                                    font=("yu gothic ui", 17, "bold"))
#         self.sign_in_label.place(x=650, y=240)

#         # Username Entry
#         self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
#                                     font=("yu gothic ui", 13, "bold"))
#         self.username_label.place(x=550, y=300)

#         self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
#                                     font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
#         self.username_entry.place(x=580, y=335, width=270)

#         self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#         self.username_line.place(x=550, y=359)
        
#         # Username icon
#         self.username_icon = Image.open('Frontend/scripts/images/username_icon.png')
#         photo = ImageTk.PhotoImage(self.username_icon)
#         self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.username_icon_label.image = photo
#         self.username_icon_label.place(x=550, y=332)

#         # Password Entry
#         self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
#                                     font=("yu gothic ui", 13, "bold"))
#         self.password_label.place(x=550, y=380)

#         self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
#                                     font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
#         self.password_entry.place(x=580, y=416, width=244)

#         self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#         self.password_line.place(x=550, y=440)
        
#         # Password icon
#         self.password_icon = Image.open('Frontend/scripts/images/password_icon.png')
#         photo = ImageTk.PhotoImage(self.password_icon)
#         self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.password_icon_label.image = photo
#         self.password_icon_label.place(x=550, y=414)

#         # Show/hide password
#         self.show_image = ImageTk.PhotoImage(file='Frontend/scripts/images/show.png')
#         self.hide_image = ImageTk.PhotoImage(file='Frontend/scripts/images/hide.png')

#         self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
#                                   activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
#         self.show_button.place(x=860, y=420)

#         # Login button
#         self.lgn_button = Image.open('Frontend/scripts/images/btn1.png')
#         photo = ImageTk.PhotoImage(self.lgn_button)
#         self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.lgn_button_label.image = photo
#         self.lgn_button_label.place(x=550, y=450)

#         self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
#                             bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.authenticate_user)
#         self.login.place(x=20, y=10)

#         # Forgot Password
#         self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
#                                     font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
#                                     activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
#         self.forgot_button.place(x=630, y=510)

#         # Sign Up
#         self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
#                                 relief=FLAT, borderwidth=0, background="#040405", fg='white')
#         self.sign_label.place(x=550, y=560)

#         self.signup_img = ImageTk.PhotoImage(file='Frontend/scripts/images/register.png')
#         self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
#                                           borderwidth=0, background="#040405", activebackground="#040405", command=self.go_to_signup)
#         self.signup_button_label.place(x=670, y=555, width=111, height=35)

#     def authenticate_user(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         try:
#             response = requests.post('http://127.0.0.1:8000/api/login', data={'username': username, 'password': password})
#             data = response.json()

#             if response.status_code == 200:
#                 self.show_message("Login successful!")
#             else:
#                 self.show_message(data.get("message", "Login failed!"))
#         except Exception as e:
#             self.show_message("Error connecting to server!")

#     def show_message(self, message):
#         messagebox.showinfo("Login Info", message)

#     def show(self):
#         self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
#                                   activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
#         self.hide_button.place(x=860, y=420)
#         self.password_entry.config(show='')

#     def hide(self):
#         self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
#                                   activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
#         self.show_button.place(x=860, y=420)
#         self.password_entry.config(show='*')

#     def go_to_signup(self):
#         self.window.destroy()
#         RegisterApp()

# def signup_page():
#     window = Tk()
#     window.title("Register")
#     window.geometry('925x500+300+200')
#     window.configure(bg='#fff')
#     window.resizable(False, False)

#     def signup():
#         username = user.get()
#         email = email_entry.get()
#         password = code.get()
#         confirm_password = confirm_code.get()

#         if password != confirm_password:
#             messagebox.showerror('Error', 'Passwords do not match')
#             return

#         try:
#             response = requests.post('http://127.0.0.1:8000/api/register',
#                                      data={'username': username, 'email': email, 'password': password})
#             if response.status_code == 201:
#                 messagebox.showinfo('Success', 'Account created successfully')
#             else:
#                 messagebox.showerror('Error', 'Failed to create account')
#         except Exception as e:
#             messagebox.showerror('Error', 'Failed to connect to the server')

#     img = Image.open('Frontend/scripts/images/login.png')
#     img = img.resize((300, 300))
#     img = ImageTk.PhotoImage(img)
#     Label(window, image=img, bg='white').place(x=50, y=50)

#     frame = Frame(window, width=350, height=350, bg='white')
#     frame.place(x=480, y=70)

#     heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
#     heading.place(x=100, y=5)

#     # User entry
#     user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
#     user.place(x=30, y=80)
#     user.insert(0, 'Username')

#     Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#     # Email entry
#     email_entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
#     email_entry.place(x=30, y=150)
#     email_entry.insert(0, 'Email')

#     Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#     # Password entry
#     code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
#     code.place(x=30, y=220)
#     code.insert(0, 'Password')

#     Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

#     # Confirm password entry
#     confirm_code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
#     confirm_code.place(x=30, y=290)
#     confirm_code.insert(0, 'Confirm Password')

#     Frame(frame, width=295, height=2, bg='black').place(x=25, y=317)

#     # Sign up button
#     Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
#                                                                                                                y=340)
#     label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
#     label.place(x=90, y=390)

#     sign_in_button = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8',
#                             command=lambda: switch_to_login(window))
#     sign_in_button.place(x=200, y=390)

#     window.mainloop()

# def switch_to_login(signup_window):
#     signup_window.destroy()
#     window = Tk()
#     LoginPage(window)
#     window.mainloop()

# if __name__ == "__main__":
#     root = Tk()
#     LoginPage(root)
#     root.mainloop()

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import ImageTk, Image
from register import RegisterApp

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # Background image
        self.bg_frame = Image.open('Frontend/scripts/images/background1.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.window, image=self.bg_photo)
        self.bg_panel.image = self.bg_photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Login Frame
        self.lgn_frame = tk.Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # Welcome Heading
        self.heading = tk.Label(self.lgn_frame, text="WELCOME", font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=tk.FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # Left Side Image
        self.side_image = Image.open('Frontend/scripts/images/vector.png')
        self.side_photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = tk.Label(self.lgn_frame, image=self.side_photo, bg='#040405')
        self.side_image_label.image = self.side_photo
        self.side_image_label.place(x=5, y=100)

        # Sign In Image
        self.sign_in_image = Image.open('Frontend/scripts/images/hyy.png')
        self.sign_in_photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = tk.Label(self.lgn_frame, image=self.sign_in_photo, bg='#040405')
        self.sign_in_image_label.image = self.sign_in_photo
        self.sign_in_image_label.place(x=620, y=130)

        # Sign In Label
        self.sign_in_label = tk.Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # Username Entry
        self.username_label = tk.Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = tk.Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = tk.Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        
        # Username icon
        self.username_icon = Image.open('Frontend/scripts/images/username_icon.png')
        self.username_icon_photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = tk.Label(self.lgn_frame, image=self.username_icon_photo, bg='#040405')
        self.username_icon_label.image = self.username_icon_photo
        self.username_icon_label.place(x=550, y=332)

        # Password Entry
        self.password_label = tk.Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = tk.Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = tk.Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        
        # Password icon
        self.password_icon = Image.open('Frontend/scripts/images/password_icon.png')
        self.password_icon_photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = tk.Label(self.lgn_frame, image=self.password_icon_photo, bg='#040405')
        self.password_icon_label.image = self.password_icon_photo
        self.password_icon_label.place(x=550, y=414)

        # Show/Hide Password
        self.show_image = ImageTk.PhotoImage(file='Frontend/scripts/images/show.png')
        self.hide_image = ImageTk.PhotoImage(file='Frontend/scripts/images/hide.png')

        self.show_button = tk.Button(self.lgn_frame, image=self.show_image, command=self.toggle_password_visibility, relief=tk.FLAT,
                                  activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.show_button.place(x=860, y=420)

        # Login Button
        self.lgn_button_image = Image.open('Frontend/scripts/images/btn1.png')
        self.lgn_button_photo = ImageTk.PhotoImage(self.lgn_button_image)
        self.lgn_button_label = tk.Label(self.lgn_frame, image=self.lgn_button_photo, bg='#040405')
        self.lgn_button_label.image = self.lgn_button_photo
        self.lgn_button_label.place(x=550, y=450)

        self.login = tk.Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.authenticate_user)
        self.login.place(x=20, y=10)

        # Forgot Password
        self.forgot_button = tk.Button(self.lgn_frame, text="Forgot Password ?", font=("yu gothic ui", 13, "bold underline"), fg="white", relief=tk.FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        # Sign Up
        self.sign_label = tk.Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=tk.FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='Frontend/scripts/images/register.png')
        self.signup_button_label = tk.Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405", command=self.go_to_signup)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.show_message("Please fill out all fields!")
            return

        try:
            response = requests.post('http://127.0.0.1:8000/api/login', data={'username': username, 'password': password})
            if response.status_code == 200:
                self.show_message("Login successful!")
            else:
                data = response.json()
                self.show_message(data.get("message", "Login failed!"))
        except Exception as e:
            self.show_message("Error connecting to server!")

    def show_message(self, message):
        messagebox.showinfo("Login Info", message)

    def toggle_password_visibility(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
            self.show_button.config(image=self.hide_image, command=self.toggle_password_visibility)
        else:
            self.password_entry.config(show='*')
            self.show_button.config(image=self.show_image, command=self.toggle_password_visibility)

    def go_to_signup(self):
        self.window.destroy()  # Close the login window
        register_window = tk.Tk()  # Create a new Tkinter window for registration
        RegisterApp(register_window)  # Initialize the RegisterApp with the new window
        register_window.mainloop()  # Start the Tkinter event loop for the registration window

if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()


