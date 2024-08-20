# tkinter_app.py (Tkinter)
import tkinter as tk
import requests

def fetch_data():
    response = requests.get('http://localhost:8000/api/example/')
    data = response.json()
    label.config(text=data['message'])

root = tk.Tk()
root.title("Tkinter with Django")

button = tk.Button(root, text="Fetch Data", command=fetch_data)
button.pack(pady=20)

label = tk.Label(root, text="")
label.pack(pady=20)

root.mainloop() 
# Frontend\scripts\main.py