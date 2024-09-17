import tkinter as tk
from Home import HomePage
from about import AboutPage
from Contact import ContactPage

class EduExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Edu Explorer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Background color for the main window

        self.create_header()
        self.create_footer()
        self.create_content_frame()
        self.navigate_to("Home")  # Default to Home page

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)
        header_frame.pack(fill=tk.X)

        header_text = tk.Label(header_frame, text="Edu Explorer", font=("Helvetica", 24, "bold"), fg="white", bg="#007acc")
        header_text.pack(side=tk.LEFT, padx=20, pady=10)

        routes_frame = tk.Frame(header_frame, bg="#007acc")
        routes_frame.pack(side=tk.RIGHT, padx=20, pady=10)

        home_button = tk.Button(routes_frame, text="Home", font=("Helvetica", 12), bg="white", fg="#007acc",
                                activebackground="#005a99", activeforeground="white",
                                command=lambda: self.navigate_to("Home"))
        home_button.pack(side=tk.LEFT, padx=10)

        about_button = tk.Button(routes_frame, text="About", font=("Helvetica", 12), bg="white", fg="#007acc",
                                 activebackground="#005a99", activeforeground="white",
                                 command=lambda: self.navigate_to("About"))
        about_button.pack(side=tk.LEFT, padx=10)

        contact_button = tk.Button(routes_frame, text="Contact", font=("Helvetica", 12), bg="white", fg="#007acc",
                                   activebackground="#005a99", activeforeground="white",
                                   command=lambda: self.navigate_to("Contact"))
        contact_button.pack(side=tk.LEFT, padx=10)

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        footer_text = tk.Label(footer_frame, text="© 2024 Edu Explorer | All Rights Reserved | Licensed under MIT License",
                               font=("Helvetica", 10), fg="white", bg="#007acc")
        footer_text.pack(side=tk.LEFT, padx=20, pady=10)

        additional_info = tk.Label(footer_frame, text="Privacy Policy | Terms of Service | Contact: support@eduexplorer.com",
                                   font=("Helvetica", 10), fg="white", bg="#007acc")
        additional_info.pack(side=tk.RIGHT, padx=20, pady=10)

    def create_content_frame(self):
        self.content_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def navigate_to(self, route):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if route == "Home":
            HomePage(self.content_frame)
        elif route == "About":
            AboutPage(self.content_frame)
        elif route == "Contact":
            ContactPage(self.content_frame)
        else:
            label = tk.Label(self.content_frame, text="Page not found", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
            label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = EduExplorerApp(root)
    root.mainloop()
