import tkinter as tk
import requests
from tkinter import messagebox

def fetch_courses():
    # Define the API URL
    url = "http://127.0.0.1:8000/api/courses/"
    
    # Replace this with your actual token
    token = "f67327ea1c7286cff49ea480a6f3ad16644c4057"  # Ensure this token is valid and correctly formatted
    
    # Set the headers with the Bearer token for authentication
    headers = {
        "Authorization": f"Token {token}",  # Changed Bearer to Token if required by your API
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error", f"Failed to fetch courses: {response.status_code}\n{response.text}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

def display_courses():
    courses = fetch_courses()
    if courses:
        course_listbox.delete(0, tk.END)  # Clear the listbox
        for course in courses:
            # Add each course title to the listbox
            course_listbox.insert(tk.END, f"{course['title']}: {course['description']}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Courses")

# Create a Listbox to display the courses
course_listbox = tk.Listbox(root, width=100, height=20)
course_listbox.pack(pady=20)

# Create a Button to trigger the fetching of courses
fetch_button = tk.Button(root, text="Fetch Courses", command=display_courses)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
