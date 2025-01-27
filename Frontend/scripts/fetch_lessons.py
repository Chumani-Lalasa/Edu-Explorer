import tkinter as tk
import requests
from tkinter import messagebox

def fetch_lessons(course_id):
    # Define the API URL for lessons based on the course_id
    url = f"http://127.0.0.1:8000/courses/{course_id}/lessons/"
    
    # Replace this with your actual token
    token = "3502b1c84c8f1ba90c78d34f05ea506a9c7c0491"  # Ensure this token is valid and correctly formatted
    
    # Set the headers with the Bearer token for authentication
    headers = {
        "Authorization": f"Token {token}",  # Changed Bearer to Token if required by your API
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the API to fetch lessons for the course
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error", f"Failed to fetch lessons: {response.status_code}\n{response.text}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

def display_lessons():
    # Get the course ID from the entry field
    course_id = course_id_entry.get()
    if not course_id:
        messagebox.showerror("Error", "Please enter a valid Course ID")
        return
    
    lessons = fetch_lessons(course_id)
    if lessons:
        lesson_listbox.delete(0, tk.END)  # Clear the listbox
        for lesson in lessons:
            # Add each lesson title and description to the listbox
            lesson_listbox.insert(tk.END, f"{lesson['title']}: {lesson['description']}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Lessons")

# Create a Label and Entry to get the Course ID from the user
tk.Label(root, text="Enter Course ID:").pack(pady=10)
course_id_entry = tk.Entry(root)
course_id_entry.pack(pady=10)

# Create a Listbox to display the lessons
lesson_listbox = tk.Listbox(root, width=100, height=20)
lesson_listbox.pack(pady=20)

# Create a Button to trigger the fetching of lessons
fetch_button = tk.Button(root, text="Fetch Lessons", command=display_lessons)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
