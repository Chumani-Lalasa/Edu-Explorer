import tkinter as tk
from tkinter import messagebox, ttk
import requests

class LessonsPage:
    def __init__(self, window):
        self.window = window
        self.window.title("Lessons - Edu Explorer")
        self.window.geometry("800x600")
        self.window.configure(bg="#f0f0f0")

        # Header Frame
        self.header_frame = tk.Frame(self.window, bg="#007acc", bd=2, relief=tk.RAISED)
        self.header_frame.pack(fill=tk.X)

        # Header Text
        self.header_text = tk.Label(self.header_frame, text="Edu Explorer - Lessons", font=("Helvetica", 24, "bold"),
                                    fg="white", bg="#007acc")
        self.header_text.pack(side=tk.LEFT, padx=20, pady=10)

        # Navigation Buttons
        self.routes_frame = tk.Frame(self.header_frame, bg="#007acc")
        self.routes_frame.pack(side=tk.RIGHT, padx=20, pady=10)
        self.create_nav_button("Home", self.routes_frame)
        self.create_nav_button("About", self.routes_frame)
        self.create_nav_button("Contact", self.routes_frame)

        # Content Area
        self.content_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Lessons Label
        self.lessons_label = tk.Label(self.content_frame, text="Available Lessons", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.lessons_label.pack(pady=10)

        # Treeview for lessons
        self.tree = self.create_treeview(self.content_frame)

        # Fetch and display lessons
        self.fetch_lessons()

    def create_nav_button(self, text, parent_frame):
        button = tk.Button(parent_frame, text=text, font=("Helvetica", 12), bg="white", fg="#007acc",
                           activebackground="#005a99", activeforeground="white",
                           command=lambda: self.navigate_to(text))
        button.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        columns = ("ID", "Title", "Description", "Duration")
        tree = ttk.Treeview(parent_frame, columns=columns, show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Description", text="Description")
        tree.heading("Duration", text="Duration")
        tree.column("ID", width=50, anchor='center')
        tree.column("Title", width=200, anchor='w')
        tree.column("Description", width=350, anchor='w')
        tree.column("Duration", width=100, anchor='center')
        tree.pack(fill=tk.BOTH, expand=True)
        return tree

    def navigate_to(self, route):
        print(f"Navigating to {route}")
        messagebox.showinfo("Navigation", f"Navigating to {route} page!")

    def fetch_lessons(self):
        api_url = 'http://127.0.0.1:8000/api/lessons/'  # Update with actual API endpoint

        try:
            response = requests.get(api_url)
            response.raise_for_status()

            lessons = response.json()
            self.display_lessons(lessons)

            print("Lessons data fetched and displayed successfully.")

        except requests.exceptions.RequestException as req_err:
            error_message = f"An error occurred: {req_err}"
            print(error_message)
            messagebox.showerror("Error", error_message)

    def display_lessons(self, lessons):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data
        for lesson in lessons:
            self.tree.insert('', tk.END, values=(
                lesson.get('id'),
                lesson.get('title'),
                lesson.get('description'),
                lesson.get('duration')
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = LessonsPage(root)
    root.mainloop()
