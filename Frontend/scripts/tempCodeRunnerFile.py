import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def on_get_started():
    messagebox.showinfo("Get Started", "Welcome to the project! Let's get started.")

def create_landing_page():
    root = tk.Tk()
    root.title("Project Landing Page")
    root.geometry("800x600")
    root.configure(bg="#4facfe")

    # Load the image from the URL
    url = "https://img.freepik.com/free-vector/students-using-e-learning-platform-video-laptop-graduation-cap_335657-3285.jpg?w=740&t=st=1724232397~exp=1724232997~hmac=276fcf3c2fd966d8e125c076b989f68bf7d280e7b713539c51afe101aa7fb0fd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image = image.resize((200, 200), Image.LANCZOS)  # Use Image.LANCZOS for resizing
        image = ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Failed to load or process the image: {e}")
        return

    # Main container frame
    container = tk.Frame(root, bg="#00f2fe", padx=20, pady=20)
    container.place(relx=0.5, rely=0.5, anchor="center")

    # Image label
    image_label = tk.Label(container, image=image, bg="#00f2fe")
    image_label.image = image  # Keep a reference to avoid garbage collection
    image_label.pack(pady=(10, 10))

    # Title
    title_label = tk.Label(container, text="Welcome to Our Project", font=("Segoe UI", 28, "bold"), bg="#00f2fe", fg="white")
    title_label.pack(pady=(10, 20))

    # Description
    desc_label = tk.Label(container, text="This project is designed to showcase the power of Python and Tkinter in building modern GUI applications. Explore the features and get started!", font=("Segoe UI", 14), bg="#00f2fe", fg="white", wraplength=600, justify="center")
    desc_label.pack(pady=(0, 30))

    # Get Started Button
    get_started_button = tk.Button(container, text="Get Started", font=("Segoe UI", 16, "bold"), bg="#ff6b6b", fg="white", padx=20, pady=10, bd=0, relief="ridge", command=on_get_started)
    get_started_button.pack()

    # Run the main loop
    root.mainloop()

# Run the landing page
create_landing_page()
