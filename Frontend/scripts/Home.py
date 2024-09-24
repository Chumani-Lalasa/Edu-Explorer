# import tkinter as tk
# from tkinter import ttk

# class HomePage:
#     def __init__(self, parent_frame):
#         self.frame = tk.Frame(parent_frame, bg="#f0f0f0")
#         self.frame.pack(fill=tk.BOTH, expand=True)
#         self.create_widgets()

#     def create_widgets(self):
#         # Navigation bar at the top
#         nav_frame = tk.Frame(self.frame, bg="#004080", height=50)
#         nav_frame.pack(fill=tk.X)

#         # Navigation buttons
#         courses_btn = tk.Button(nav_frame, text="Courses", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_courses)
#         courses_btn.pack(side=tk.LEFT, padx=10, pady=10)

#         lessons_btn = tk.Button(nav_frame, text="Lessons", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_lessons)
#         lessons_btn.pack(side=tk.LEFT, padx=10, pady=10)

#         quizzes_btn = tk.Button(nav_frame, text="Quizzes", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white", command=self.show_quizzes)
#         quizzes_btn.pack(side=tk.LEFT, padx=10, pady=10)

#         # Content area
#         self.content_frame = tk.Frame(self.frame, bg="#f0f0f0")
#         self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

#         # Show Courses by default
#         self.show_courses()

#     def clear_content(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#     def show_courses(self):
#         self.clear_content()
#         title = tk.Label(self.content_frame, text="Courses", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
#         title.pack(pady=10)

#         # Display courses in card-like layout
#         self.create_card("Python for Beginners", "A complete guide to Python programming.")
#         self.create_card("Advanced Java", "Dive deeper into Java with this advanced course.")
#         self.create_card("Web Development", "Learn to build websites from scratch.")

#     def show_lessons(self):
#         self.clear_content()
#         title = tk.Label(self.content_frame, text="Lessons", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
#         title.pack(pady=10)

#         # Display lessons in card-like layout
#         self.create_card("Python Functions", "Understand how functions work in Python.")
#         self.create_card("Java Inheritance", "Learn about object-oriented programming in Java.")
#         self.create_card("HTML & CSS Basics", "Basics of web development using HTML and CSS.")

#     def show_quizzes(self):
#         self.clear_content()
#         title = tk.Label(self.content_frame, text="Quizzes", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
#         title.pack(pady=10)

#         # Display quizzes in card-like layout
#         self.create_card("Python Quiz", "Test your knowledge of Python programming.")
#         self.create_card("Java Basics Quiz", "Quiz on the basic concepts of Java.")
#         self.create_card("HTML/CSS Quiz", "Test your web development skills.")

#     def create_card(self, title, description):
#         # Create a card-like frame
#         card_frame = tk.Frame(self.content_frame, bg="white", bd=2, relief=tk.RIDGE)
#         card_frame.pack(pady=10, padx=20, fill=tk.X)

#         # Course/Lesson/Quiz Title
#         title_label = tk.Label(card_frame, text=title, font=("Helvetica", 16, "bold"), bg="white")
#         title_label.pack(anchor="w", pady=5, padx=10)

#         # Description
#         desc_label = tk.Label(card_frame, text=description, font=("Helvetica", 12), bg="white")
#         desc_label.pack(anchor="w", pady=5, padx=10)

#         # Enroll or View Details button
#         action_button = tk.Button(card_frame, text="View Details", font=("Helvetica", 12), bg="#004080", fg="white")
#         action_button.pack(side=tk.RIGHT, padx=10, pady=10)


# # Root window
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#     root.title("Edu Explorer")
#     app = HomePage(root)
#     root.mainloop()




import tkinter as tk
from fetch_course import fetch_courses  # Import the function to fetch courses

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

        # Create a frame for the content area
        self.content_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        # Set up scrollable area
        self.canvas = tk.Canvas(self.content_frame, bg="#f0f0f0")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0")

        # Bind the scrollable frame to the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)  # For Windows
        self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)  # For Linux
        self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)  # For Linux

        # Show Courses by default
        self.show_courses()

    def clear_content(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def show_courses(self):
        self.clear_content()
        title = tk.Label(self.scrollable_frame, text="Courses", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Fetch the courses from the backend
        courses = fetch_courses()
        if courses:
            for course in courses:
                self.create_card(course['title'], course['description'])
        else:
            no_data_label = tk.Label(self.scrollable_frame, text="No courses available", font=("Helvetica", 14), bg="#f0f0f0")
            no_data_label.pack(pady=20)

    def show_lessons(self):
        self.clear_content()
        title = tk.Label(self.scrollable_frame, text="Lessons", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)
        self.create_card("Python Functions", "Understand how functions work in Python.")
        self.create_card("Java Inheritance", "Learn about object-oriented programming in Java.")
        self.create_card("HTML & CSS Basics", "Basics of web development using HTML and CSS.")

    def show_quizzes(self):
        self.clear_content()
        title = tk.Label(self.scrollable_frame, text="Quizzes", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)
        self.create_card("Python Quiz", "Test your knowledge of Python programming.")
        self.create_card("Java Basics Quiz", "Quiz on the basic concepts of Java.")
        self.create_card("HTML/CSS Quiz", "Test your web development skills.")

    def create_card(self, title, description):
        # Create a card-like frame that takes full width
        card_frame = tk.Frame(self.scrollable_frame, bg="white", bd=2, relief=tk.RIDGE)
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

    def on_mouse_wheel(self, event):
        # Scroll up or down depending on the event direction
        if event.num == 5 or event.delta == -120:  # Scroll down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # Scroll up
            self.canvas.yview_scroll(-1, "units")


# Root window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Edu Explorer")
    app = HomePage(root)
    root.mainloop()
