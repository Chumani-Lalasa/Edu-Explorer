from tkinter import *
from PIL import ImageTk, Image

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0,0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        self.bg_frame = Image.open('images\\')
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()
if __name__ == 'main':
    page()