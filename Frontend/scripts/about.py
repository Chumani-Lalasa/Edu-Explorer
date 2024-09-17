# import tkinter as tk

# # Function to navigate to different routes
# def navigate_to(route):
#     # This would be where the logic for changing frames or opening new windows goes
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

# # Use separate labels for each paragraph to control spacing and layout more precisely
# about_text_1 = tk.Label(content_frame, text=(
#     "Edu Explorer is a comprehensive platform designed to facilitate and enhance the learning experience. "
#     "Our goal is to provide users with access to high-quality educational resources, tutorials, and quizzes, "
#     "all in one place. Whether you are a student looking to improve your knowledge or an educator seeking to "
#     "share your expertise, Edu Explorer offers a range of tools and features to support your educational journey."
# ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
# about_text_1.pack(pady=15)  # Increased padding here

# about_text_2 = tk.Label(content_frame, text=(
#     "At Edu Explorer, we believe that education should be engaging, accessible, and inclusive. Whether you're preparing "
#     "for an upcoming exam, exploring new subjects, or improving existing skills, our platform offers a variety of courses, "
#     "interactive quizzes, and educational tutorials tailored to meet individual learning needs."
# ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
# about_text_2.pack(pady=15)  # Increased padding here

# about_text_3 = tk.Label(content_frame, text=(
#     "For educators, we provide a suite of tools designed to enhance teaching efficiency, including options for creating "
#     "custom quizzes, tracking student progress, and sharing expertise with a global audience. Our goal is to foster a collaborative "
#     "environment where students and educators alike can share knowledge, improve skills, and grow together as part of a vibrant learning community."
# ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
# about_text_3.pack(pady=15)  # Increased padding here

# about_text_4 = tk.Label(content_frame, text=(
#     "Explore Edu Explorer today and become part of a community committed to making learning an exciting and rewarding journey."
# ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
# about_text_4.pack(pady=15)  # Increased padding here

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

# # Run the application with a try-except block for error handling
# try:
#     root.mainloop()
# except Exception as e:
#     print(f"An error occurred: {e}")
# About.py
import tkinter as tk

class AboutPage:
    def __init__(self, parent):
        self.parent = parent
        self.create_about_page()

    def create_about_page(self):
        # Clear previous content (if any)
        for widget in self.parent.winfo_children():
            widget.destroy()

        # About page title
        about_title = tk.Label(self.parent, text="About Edu Explorer", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        about_title.pack(pady=20)

        # Paragraphs describing the platform
        about_text_1 = tk.Label(self.parent, text=(
            "Edu Explorer is a comprehensive platform designed to facilitate and enhance the learning experience. "
            "Our goal is to provide users with access to high-quality educational resources, tutorials, and quizzes, "
            "all in one place. Whether you are a student looking to improve your knowledge or an educator seeking to "
            "share your expertise, Edu Explorer offers a range of tools and features to support your educational journey."
        ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
        about_text_1.pack(pady=15)

        about_text_2 = tk.Label(self.parent, text=(
            "At Edu Explorer, we believe that education should be engaging, accessible, and inclusive. Whether you're preparing "
            "for an upcoming exam, exploring new subjects, or improving existing skills, our platform offers a variety of courses, "
            "interactive quizzes, and educational tutorials tailored to meet individual learning needs."
        ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
        about_text_2.pack(pady=15)

        about_text_3 = tk.Label(self.parent, text=(
            "For educators, we provide a suite of tools designed to enhance teaching efficiency, including options for creating "
            "custom quizzes, tracking student progress, and sharing expertise with a global audience. Our goal is to foster a collaborative "
            "environment where students and educators alike can share knowledge, improve skills, and grow together as part of a vibrant learning community."
        ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
        about_text_3.pack(pady=15)

        about_text_4 = tk.Label(self.parent, text=(
            "Explore Edu Explorer today and become part of a community committed to making learning an exciting and rewarding journey."
        ), font=("Helvetica", 12), bg="#f0f0f0", wraplength=760)
        about_text_4.pack(pady=15)

        # Optional: Add an image, logo, or any other graphical content for the About page
        # For example, if you want to display an image:
        # image = tk.PhotoImage(file="path/to/your/image.png")
        # image_label = tk.Label(self.parent, image=image, bg="#f0f0f0")
        # image_label.image = image  # Keep a reference to avoid garbage collection
        # image_label.pack(pady=20)

        # Add any additional buttons or navigation items as needed
        # For example, a "Learn More" button could be added below the text
        learn_more_button = tk.Button(self.parent, text="Learn More", font=("Helvetica", 12), bg="#007acc", fg="white",
                                      command=self.learn_more_action)
        learn_more_button.pack(pady=20)

    # Sample action for the "Learn More" button
    def learn_more_action(self):
        print("Redirecting to more information about Edu Explorer...")

