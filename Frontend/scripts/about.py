# import tkinter as tk

# # Function to navigate to different routes
# def navigate_to(route):
#     print(f"Navigating to {route}")

# # Create the main window
# root = tk.Tk()
# root.title("About - Edu Explorer")
# root.geometry("800x600")
# root.configure(bg="#f0f0f0")  # Background color for the main window

# # Header frame
# header_frame = tk.Frame(root, bg="#007acc", bd=2, relief=tk.RAISED)  # Dark blue header with raised border
# header_frame.pack(fill=tk.X)

# # Header text (acting as a placeholder for the logo and middle image)
# header_text = tk.Label(header_frame, text="Edu Explorer", font=("Helvetica", 24, "bold"), fg="white", bg="#007acc")
# header_text.pack(side=tk.LEFT, padx=20, pady=10)

# # Routes in the header
# routes_frame = tk.Frame(header_frame, bg="#007acc")
# routes_frame.pack(side=tk.RIGHT, padx=20, pady=10)

# home_button = tk.Button(routes_frame, text="Home", font=("Helvetica", 12), bg="white", fg="#007acc",
#                         activebackground="#005a99", activeforeground="white",
#                         command=lambda: navigate_to("Home"))
# home_button.pack(side=tk.LEFT, padx=10)

# about_button = tk.Button(routes_frame, text="About", font=("Helvetica", 12), bg="white", fg="#007acc",
#                          activebackground="#005a99", activeforeground="white",
#                          command=lambda: navigate_to("About"))
# about_button.pack(side=tk.LEFT, padx=10)

# contact_button = tk.Button(routes_frame, text="Contact", font=("Helvetica", 12), bg="white", fg="#007acc",
#                            activebackground="#005a99", activeforeground="white",
#                            command=lambda: navigate_to("Contact"))
# contact_button.pack(side=tk.LEFT, padx=10)

# # Main content area
# content_frame = tk.Frame(root, bg="#f0f0f0")
# content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# # About content
# about_label = tk.Label(content_frame, text="About Edu Explorer", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
# about_label.pack(pady=20)

# about_text = tk.Label(content_frame, text=(
#     "Edu Explorer is a comprehensive platform designed to facilitate and enhance the learning experience. "
#     "Our goal is to provide users with access to high-quality educational resources, tutorials, and quizzes, "
#     "all in one place. Whether you are a student looking to improve your knowledge or an educator seeking to "
#     "share your expertise, Edu Explorer offers a range of tools and features to support your educational journey. "
#     "Explore our platform to discover a variety of learning materials and engage with a community of learners and educators."
# ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
# about_text.pack(pady=10)

# # Footer frame (similar to the header)
# footer_frame = tk.Frame(root, bg="#007acc", bd=2, relief=tk.RAISED)
# footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# # Footer text (adding license information and other details)
# footer_text = tk.Label(footer_frame, text="© 2024 Edu Explorer | All Rights Reserved | Licensed under MIT License", 
#                        font=("Helvetica", 10), fg="white", bg="#007acc")
# footer_text.pack(side=tk.LEFT, padx=20, pady=10)

# # Additional footer information
# additional_info = tk.Label(footer_frame, text="Privacy Policy | Terms of Service | Contact: support@eduexplorer.com", 
#                            font=("Helvetica", 10), fg="white", bg="#007acc")
# additional_info.pack(side=tk.RIGHT, padx=20, pady=10)

# # Run the application
# root.mainloop()
import tkinter as tk

class AboutPage:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#f0f0f0")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        about_label = tk.Label(self.frame, text="About Edu Explorer", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        about_label.pack(pady=20)

        about_text = tk.Label(self.frame, text=(
            "Edu Explorer is a comprehensive platform designed to facilitate and enhance the learning experience. "
            "Our goal is to provide users with access to high-quality educational resources, tutorials, and quizzes, "
            "all in one place. Whether you are a student looking to improve your knowledge or an educator seeking to "
            "share your expertise, Edu Explorer offers a range of tools and features to support your educational journey. "
            "Explore our platform to discover a variety of learning materials and engage with a community of learners and educators."
        ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
        about_text.pack(pady=10)
