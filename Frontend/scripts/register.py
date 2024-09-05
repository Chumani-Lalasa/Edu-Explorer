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
        self.resized_image = self.image.resize((925, 500), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.resized_image)

        # Set the image as the background of the window
        self.bg_label = Label(self.window, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Registration Frame
        self.reg_frame = Frame(self.window, bg='#fff', width=400, height=350)
        self.reg_frame.place(x=500, y=80)

        # Heading
        self.heading = Label(self.reg_frame, text='Create Account', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='#fff')
        self.heading.place(x=50, y=15)

        # Username Entry
        self.username_label = Label(self.reg_frame, text='Username', font=('Microsoft Yahei UI Light', 12), bg='#fff')
        self.username_label.place(x=50, y=80)
        self.username_entry = Entry(self.reg_frame, font=('Microsoft Yahei UI Light', 12), bd=1, bg='#eee', insertbackground='black')
        self.username_entry.place(x=50, y=105, width=300)

        # Email Entry
        self.email_label = Label(self.reg_frame, text='Email', font=('Microsoft Yahei UI Light', 12), bg='#fff')
        self.email_label.place(x=50, y=140)
        self.email_entry = Entry(self.reg_frame, font=('Microsoft Yahei UI Light', 12), bd=1, bg='#eee', insertbackground='black')
        self.email_entry.place(x=50, y=165, width=300)

        # Password Entry
        self.password_label = Label(self.reg_frame, text='Password', font=('Microsoft Yahei UI Light', 12), bg='#fff')
        self.password_label.place(x=50, y=200)
        self.password_entry = Entry(self.reg_frame, font=('Microsoft Yahei UI Light', 12), bd=1, bg='#eee', insertbackground='black', show='*')
        self.password_entry.place(x=50, y=225, width=300)

        # Register Button
        self.register_button = Button(self.reg_frame, text='Register', font=('Microsoft Yahei UI Light', 12, 'bold'), bg='#57a1f8', fg='white', command=self.register_user)
        self.register_button.place(x=50, y=270, width=300, height=35)

        # Login Button
        self.login_button = Button(self.reg_frame, text='Already have an account? Login', font=('Microsoft Yahei UI Light', 10), bg='#fff', fg='#57a1f8', command=self.go_to_login)
        self.login_button.place(x=50, y=320, width=300)

    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not username or not email or not password:
            self.show_message("Please fill all fields!")
            return

        try:
            response = requests.post('http://127.0.0.1:8000/api/register/', data={'username': username, 'email': email, 'password': password})
            data = response.json()

            if response.status_code == 201:
                self.show_message("Registration successful!")
            else:
                self.show_message(data.get("message", "Registration failed!"))
        except Exception as e:
            self.show_message("Error connecting to server!")

    def show_message(self, message):
        messagebox.showinfo("Registration Info", message)

    def go_to_login(self):
        self.window.destroy()  # Close the registration window
        login_window = Tk()  # Create a new Tkinter window for login
        from login import LoginPage
        LoginPage(login_window)  # Initialize the LoginPage with the new window
        login_window.mainloop()  # Run the new login window

if __name__ == "__main__":
    root = Tk()
    app = RegisterApp(root)
    root.mainloop()
