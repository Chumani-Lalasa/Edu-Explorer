# import tkinter as tk
# from tkinter import messagebox

# # Function to navigate to different routes
# def navigate_to(route):
#     print(f"Navigating to {route}")

# # Function to handle the form submission
# def submit_form():
#     name = name_entry.get()
#     email = email_entry.get()
#     message = message_text.get("1.0", tk.END).strip()

#     if not name or not email or not message:
#         messagebox.showwarning("Input Error", "Please fill in all fields.")
#         return

#     # For demonstration purposes, we're just showing a message box
#     messagebox.showinfo("Form Submitted", "Thank you for contacting us!")
#     # Clear the form fields
#     name_entry.delete(0, tk.END)
#     email_entry.delete(0, tk.END)
#     message_text.delete("1.0", tk.END)

# # Create the main window
# root = tk.Tk()
# root.title("Contact - Edu Explorer")
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

# # Contact content
# contact_label = tk.Label(content_frame, text="Contact Us", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
# contact_label.pack(pady=20)

# contact_info = tk.Label(content_frame, text=(
#     "If you have any questions or need support, please feel free to contact us:\n\n"
#     "Email: support@eduexplorer.com\n"
#     "Phone: +1-800-123-4567\n"
#     "Address: 123 Edu Street, Learning City, LC 12345"
# ), font=("Helvetica", 12), bg="#f0f0f0")
# contact_info.pack(pady=10)

# # Contact form
# form_frame = tk.Frame(content_frame, bg="#f0f0f0")
# form_frame.pack(pady=20)

# name_label = tk.Label(form_frame, text="Name:", font=("Helvetica", 12), bg="#f0f0f0")
# name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
# name_entry = tk.Entry(form_frame, width=50)
# name_entry.grid(row=0, column=1, padx=5, pady=5)

# email_label = tk.Label(form_frame, text="Email:", font=("Helvetica", 12), bg="#f0f0f0")
# email_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
# email_entry = tk.Entry(form_frame, width=50)
# email_entry.grid(row=1, column=1, padx=5, pady=5)

# message_label = tk.Label(form_frame, text="Message:", font=("Helvetica", 12), bg="#f0f0f0")
# message_label.grid(row=2, column=0, sticky=tk.NW, padx=5, pady=5)
# message_text = tk.Text(form_frame, width=50, height=10)
# message_text.grid(row=2, column=1, padx=5, pady=5)

# submit_button = tk.Button(form_frame, text="Submit", font=("Helvetica", 12), bg="#007acc", fg="white",
#                           activebackground="#005a99", activeforeground="white", command=submit_form)
# submit_button.grid(row=3, column=1, pady=10, sticky=tk.E)

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
from tkinter import messagebox

# Function to navigate to different routes
def navigate_to(route):
    print(f"Navigating to {route}")

# Function to handle the form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_text.get("1.0", tk.END).strip()

    if not name or not email or not message:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    # For demonstration purposes, we're just showing a message box
    messagebox.showinfo("Form Submitted", "Thank you for contacting us!")
    # Clear the form fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact - Edu Explorer")
root.geometry("800x600")
root.configure(bg="#f8f8f8")  # Light grey background color for the main window

# Header frame
header_frame = tk.Frame(root, bg="#003366", bd=2, relief=tk.RAISED)  # Dark blue header with raised border
header_frame.pack(fill=tk.X)

# Header text (acting as a placeholder for the logo and middle image)
header_text = tk.Label(header_frame, text="Edu Explorer", font=("Arial", 24, "bold"), fg="white", bg="#003366")
header_text.pack(side=tk.LEFT, padx=20, pady=10)

# Routes in the header
routes_frame = tk.Frame(header_frame, bg="#003366")
routes_frame.pack(side=tk.RIGHT, padx=20, pady=10)

home_button = tk.Button(routes_frame, text="Home", font=("Arial", 12), bg="white", fg="#003366",
                        activebackground="#005a99", activeforeground="white",
                        command=lambda: navigate_to("Home"))
home_button.pack(side=tk.LEFT, padx=10)

about_button = tk.Button(routes_frame, text="About", font=("Arial", 12), bg="white", fg="#003366",
                         activebackground="#005a99", activeforeground="white",
                         command=lambda: navigate_to("About"))
about_button.pack(side=tk.LEFT, padx=10)

contact_button = tk.Button(routes_frame, text="Contact", font=("Arial", 12), bg="white", fg="#003366",
                           activebackground="#005a99", activeforeground="white",
                           command=lambda: navigate_to("Contact"))
contact_button.pack(side=tk.LEFT, padx=10)

# Main content area
content_frame = tk.Frame(root, bg="#f8f8f8")
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Contact content
contact_label = tk.Label(content_frame, text="Contact Us", font=("Arial", 24, "bold"), bg="#f8f8f8")
contact_label.pack(pady=20)

contact_info = tk.Label(content_frame, text=(
    "If you have any questions or need support, please feel free to contact us:\n\n"
    "Email: support@eduexplorer.com\n"
    "Phone: +1-800-123-4567\n"
    "Address: 123 Edu Street, Learning City, LC 12345"
), font=("Arial", 12), bg="#f8f8f8")
contact_info.pack(pady=10)

# Contact form
form_frame = tk.Frame(content_frame, bg="#f8f8f8")
form_frame.pack(pady=20)

name_label = tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f8f8f8")
name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=50, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f8f8f8")
email_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=50, font=("Arial", 12))
email_entry.grid(row=1, column=1, padx=5, pady=5)

message_label = tk.Label(form_frame, text="Message:", font=("Arial", 12), bg="#f8f8f8")
message_label.grid(row=2, column=0, sticky=tk.NW, padx=5, pady=5)
message_text = tk.Text(form_frame, width=50, height=10, font=("Arial", 12))
message_text.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(form_frame, text="Submit", font=("Arial", 12), bg="#003366", fg="white",
                          activebackground="#005a99", activeforeground="white", command=submit_form)
submit_button.grid(row=3, column=1, pady=10, sticky=tk.E)

# Footer frame (similar to the header)
footer_frame = tk.Frame(root, bg="#003366", bd=2, relief=tk.RAISED)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Footer text (adding license information and other details)
footer_text = tk.Label(footer_frame, text="© 2024 Edu Explorer | All Rights Reserved | Licensed under MIT License", 
                       font=("Arial", 10), fg="white", bg="#003366")
footer_text.pack(side=tk.LEFT, padx=20, pady=10)

# Additional footer information
additional_info = tk.Label(footer_frame, text="Privacy Policy | Terms of Service | Contact: support@eduexplorer.com", 
                           font=("Arial", 10), fg="white", bg="#003366")
additional_info.pack(side=tk.RIGHT, padx=20, pady=10)

# Run the application
root.mainloop()
