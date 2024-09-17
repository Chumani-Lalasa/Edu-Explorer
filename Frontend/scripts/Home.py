# import tkinter as tk

# class EduExplorerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Edu Explorer")
#         self.root.geometry("800x600")
#         self.root.configure(bg="#f0f0f0")  # Background color for the main window

#         self.create_header()
#         self.create_content()
#         self.create_footer()

#     # Function to navigate to different routes
#     def navigate_to(self, route):
#         print(f"Navigating to {route}")
#         # You can update this part to change the content dynamically based on the route
#         self.content_label.config(text=f"Welcome to {route} page!")

#     # Function to create the header section
#     def create_header(self):
#         # Header frame
#         header_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)  # Dark blue header with raised border
#         header_frame.pack(fill=tk.X)

#         # Header text (acting as a placeholder for the logo and middle image)
#         header_text = tk.Label(header_frame, text="Edu Explorer", font=("Helvetica", 24, "bold"), fg="white", bg="#007acc")
#         header_text.pack(side=tk.LEFT, padx=20, pady=10)

#         # Routes in the header
#         routes_frame = tk.Frame(header_frame, bg="#007acc")
#         routes_frame.pack(side=tk.RIGHT, padx=20, pady=10)

#         home_button = tk.Button(routes_frame, text="Home", font=("Helvetica", 12), bg="white", fg="#007acc",
#                                 activebackground="#005a99", activeforeground="white",
#                                 command=lambda: self.navigate_to("Home"))
#         home_button.pack(side=tk.LEFT, padx=10)

#         about_button = tk.Button(routes_frame, text="About", font=("Helvetica", 12), bg="white", fg="#007acc",
#                                  activebackground="#005a99", activeforeground="white",
#                                  command=lambda: self.navigate_to("About"))
#         about_button.pack(side=tk.LEFT, padx=10)

#         contact_button = tk.Button(routes_frame, text="Contact", font=("Helvetica", 12), bg="white", fg="#007acc",
#                                    activebackground="#005a99", activeforeground="white",
#                                    command=lambda: self.navigate_to("Contact"))
#         contact_button.pack(side=tk.LEFT, padx=10)

#     # Function to create the content area
#     def create_content(self):
#         content_frame = tk.Frame(self.root, bg="#f0f0f0")
#         content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

#         # Example content (to be updated dynamically based on route)
#         self.content_label = tk.Label(content_frame, text="Welcome to Edu Explorer", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
#         self.content_label.pack(pady=20)

#     # Function to create the footer section
#     def create_footer(self):
#         # Footer frame (similar to the header)
#         footer_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)
#         footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

#         # Footer text (adding license information and other details)
#         footer_text = tk.Label(footer_frame, text="© 2024 Edu Explorer | All Rights Reserved | Licensed under MIT License",
#                                font=("Helvetica", 10), fg="white", bg="#007acc")
#         footer_text.pack(side=tk.LEFT, padx=20, pady=10)

#         # Additional footer information
#         additional_info = tk.Label(footer_frame, text="Privacy Policy | Terms of Service | Contact: support@eduexplorer.com",
#                                    font=("Helvetica", 10), fg="white", bg="#007acc")
#         additional_info.pack(side=tk.RIGHT, padx=20, pady=10)


# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EduExplorerApp(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#f0f0f0")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Navigation bar at the top
        nav_frame = tk.Frame(self.frame, bg="#004080", height=50)
        nav_frame.pack(fill=tk.X)

        # Navigation buttons
        courses_btn = tk.Button(nav_frame, text="Courses", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_courses)
        courses_btn.pack(side=tk.LEFT, padx=10, pady=10)

        lessons_btn = tk.Button(nav_frame, text="Lessons", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_lessons)
        lessons_btn.pack(side=tk.LEFT, padx=10, pady=10)

        quizzes_btn = tk.Button(nav_frame, text="Quizzes", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_quizzes)
        quizzes_btn.pack(side=tk.LEFT, padx=10, pady=10)

        # Content area
        self.content_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        # Show Courses by default
        self.show_courses()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_courses(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="Courses", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Display courses in card-like layout
        self.create_card("Python for Beginners", "A complete guide to Python programming.")
        self.create_card("Advanced Java", "Dive deeper into Java with this advanced course.")
        self.create_card("Web Development", "Learn to build websites from scratch.")

    def show_lessons(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="Lessons", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Display lessons in card-like layout
        self.create_card("Python Functions", "Understand how functions work in Python.")
        self.create_card("Java Inheritance", "Learn about object-oriented programming in Java.")
        self.create_card("HTML & CSS Basics", "Basics of web development using HTML and CSS.")

    def show_quizzes(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="Quizzes", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Display quizzes in card-like layout
        self.create_card("Python Quiz", "Test your knowledge of Python programming.")
        self.create_card("Java Basics Quiz", "Quiz on the basic concepts of Java.")
        self.create_card("HTML/CSS Quiz", "Test your web development skills.")

    def create_card(self, title, description):
        # Create a card-like frame
        card_frame = tk.Frame(self.content_frame, bg="white", bd=2, relief=tk.RIDGE)
        card_frame.pack(pady=10, padx=20, fill=tk.X)

        # Course/Lesson/Quiz Title
        title_label = tk.Label(card_frame, text=title, font=("Helvetica", 16, "bold"), bg="white")
        title_label.pack(anchor="w", pady=5, padx=10)

        # Description
        desc_label = tk.Label(card_frame, text=description, font=("Helvetica", 12), bg="white")
        desc_label.pack(anchor="w", pady=5, padx=10)

        # Enroll or View Details button
        action_button = tk.Button(card_frame, text="View Details", font=("Helvetica", 12), bg="#004080", fg="white")
        action_button.pack(side=tk.RIGHT, padx=10, pady=10)


# Root window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Edu Explorer")
    app = HomePage(root)
    root.mainloop()



