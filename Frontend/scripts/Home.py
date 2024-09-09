import tkinter as tk

class EduExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Edu Explorer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Background color for the main window

        self.create_header()
        self.create_content()
        self.create_footer()

    # Function to navigate to different routes
    def navigate_to(self, route):
        print(f"Navigating to {route}")
        # You can update this part to change the content dynamically based on the route
        self.content_label.config(text=f"Welcome to {route} page!")

    # Function to create the header section
    def create_header(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)  # Dark blue header with raised border
        header_frame.pack(fill=tk.X)

        # Header text (acting as a placeholder for the logo and middle image)
        header_text = tk.Label(header_frame, text="Edu Explorer", font=("Helvetica", 24, "bold"), fg="white", bg="#007acc")
        header_text.pack(side=tk.LEFT, padx=20, pady=10)

        # Routes in the header
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

    # Function to create the content area
    def create_content(self):
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Example content (to be updated dynamically based on route)
        self.content_label = tk.Label(content_frame, text="Welcome to Edu Explorer", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.content_label.pack(pady=20)

    # Function to create the footer section
    def create_footer(self):
        # Footer frame (similar to the header)
        footer_frame = tk.Frame(self.root, bg="#007acc", bd=2, relief=tk.RAISED)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Footer text (adding license information and other details)
        footer_text = tk.Label(footer_frame, text="© 2024 Edu Explorer | All Rights Reserved | Licensed under MIT License",
                               font=("Helvetica", 10), fg="white", bg="#007acc")
        footer_text.pack(side=tk.LEFT, padx=20, pady=10)

        # Additional footer information
        additional_info = tk.Label(footer_frame, text="Privacy Policy | Terms of Service | Contact: support@eduexplorer.com",
                                   font=("Helvetica", 10), fg="white", bg="#007acc")
        additional_info.pack(side=tk.RIGHT, padx=20, pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EduExplorerApp(root)
    root.mainloop()
