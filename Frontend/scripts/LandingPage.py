import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from login import LoginPage  # Import the LoginPage class directly

def on_get_started(root):
    root.destroy()  # Close the landing page window
    login_window = tk.Tk()  # Create a new window for the login page
    LoginPage(login_window)  # Initialize the LoginPage class
    login_window.mainloop()

def create_landing_page():
    root = tk.Tk()
    root.title("E-Learning Platform")
    root.geometry("1166x718")  # Adjust window size for better fit

    # Load the image from the URL
    url = "https://img.freepik.com/premium-photo/elearning-future-education_1279828-1811.jpg?size=626&ext=jpg&ga=GA1.1.869934292.1698666364&semt=ais_hybrid"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image = image.resize((500, 800), Image.Resampling.LANCZOS)  # Resize image to fit the window
        image_tk = ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Failed to load or process the image: {e}")
        return

    # Create a Canvas widget for the image
    image_canvas = tk.Canvas(root, width=500, height=800, highlightthickness=0)
    image_canvas.pack(side="left", fill="both")
    image_canvas.create_image(0, 0, anchor="nw", image=image_tk)
    image_canvas.image = image_tk  # Keep a reference to avoid garbage collection

    # Create a Frame for other widgets
    content_frame = tk.Frame(root, width=700, height=800, bg="#00f2fe", padx=20, pady=20)
    content_frame.pack(side="right", fill="both", expand=True)

    # Title
    title_label = tk.Label(content_frame, text="Welcome to E-Learning Platform", font=("Segoe UI", 28, "bold"), bg="#00f2fe", fg="black")
    title_label.pack(pady=(20, 15))

    # Description
    desc_label = tk.Label(content_frame, text=(
        "Empowering Education, Anytime, Anywhere\n\n"
        "Discover the future of learning with our E-Learning Platform, designed to transform the way you access and deliver knowledge. "
        "Whether you're a student eager to learn or an instructor passionate about teaching, our platform provides a seamless experience for both.\n\n"
        "What We Offer:\n\n"
        "• Dynamic Learning Experience: Engage with interactive video lectures, comprehensive quizzes, and real-time progress tracking.\n\n"
        "• Tailored for Everyone: From students who can explore diverse courses and track their progress, to instructors who can create, manage, and share their expertise effortlessly.\n\n"
        "• Certificates of Achievement: Celebrate your milestones with certificates that validate your accomplishments and boost your career.\n\n"
        "• Innovative Course Management: Instructors can effortlessly design, update, and manage courses, ensuring a rich educational experience.\n\n"
        "• Responsive and User-Friendly: Our intuitive interface adapts to your needs, whether you're learning on-the-go or managing courses from your desktop.\n\n"
        "Join us and elevate your learning journey with a platform that adapts to your needs, inspires growth, and connects knowledge with innovation."
    ), font=("Segoe UI", 12), bg="#00f2fe", fg="black", wraplength=500, justify="left")
    desc_label.pack(pady=(0, 20))

    # Get Started Button
    get_started_button = tk.Button(
        content_frame,  # Attach the button to the content_frame
        text="Get Started",
        font=("Segoe UI", 16, "bold"),
        bg="#ff6b6b",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        relief="ridge",
        command=lambda: on_get_started(root),  # Pass root to on_get_started
        width=15,   # Set equal width
        height=2    # Set equal height
    )
    get_started_button.pack(pady=(20, 0))

    # Run the main loop
    root.mainloop()

# Run the landing page
if __name__ == "__main__":
    create_landing_page()