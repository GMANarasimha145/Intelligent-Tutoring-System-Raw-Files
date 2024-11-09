import tkinter as tk
from tkinter import messagebox, Toplevel
from pymongo import MongoClient
import pyttsx3
import time
import os
import win32com.client as win32
from pptx import Presentation  # Import the Presentation class
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def register():
    # Get user input from the entry fields
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    mobile_number = mobile_entry.get()

    # Store the user information in MongoDB
    client = MongoClient('mongodb://localhost:27017/intelligent_tutoring')
    db = client['intelligent_tutoring']
    collection = db['learners']
    user_data = {
        "username": username,
        "password": password,
        "email": email,
        "mobile_number": mobile_number
    }
    collection.insert_one(user_data)
    client.close()

def check_login():
    # Get user input from the entry fields
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Retrieve user information from MongoDB
    client = MongoClient('mongodb://localhost:27017/intelligent_tutoring')
    db = client['intelligent_tutoring']
    collection = db['learners']
    user_info = collection.find_one({"username": username, "password": password})
    client.close()

    # Check if user_info is None (username and password not found)
    if user_info:
        messagebox.showinfo("Success", "Login Successful!")
        open_second_window()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def open_second_window():
    second_window = Toplevel(root)
    second_window.title("Topic Selection")
    second_window.geometry("800x600")  # Set the size of the second window

    # Create label and entry field for topic selection
    tk.Label(second_window, text="Enter Topic Name:").pack()
    topic_entry = tk.Entry(second_window)
    topic_entry.pack()

    # Create and place Submit button
    submit_button = tk.Button(second_window, text="Submit", command=lambda: execute_presentation(topic_entry.get(), second_window))
    submit_button.pack()

def execute_presentation(topic, window):
    window.destroy()  # Close the second window

    # Call the text_generator function with the topic entered by the user
    generated_text = text_generator(topic)

    # Print the generated text to the console
    print("Generated Text:")
    print(generated_text)

def text_generator(my_text):
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

    inputs = tokenizer(my_text, return_tensors="pt")
    outputs = model.generate(**inputs, \
                            min_length=256, \
                            max_new_tokens=1024, \
                            length_penalty=0.9, \
                            num_beams=8, \
                            no_repeat_ngram_size=2, \
                            early_stopping=True)
    output_text_Flan_t5 = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return output_text_Flan_t5

# Create main window
root = tk.Tk()
root.title("Registration and Login Form")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to match screen size
root.geometry(f"{screen_width}x{screen_height}")

# Create labels and entry fields for registration
tk.Label(root, text="Username:").place(x=screen_width/3, y=screen_height/4)
username_entry = tk.Entry(root)
username_entry.place(x=screen_width/2, y=screen_height/4)

tk.Label(root, text="Password:").place(x=screen_width/3, y=screen_height/4 + 30)
password_entry = tk.Entry(root, show="*")
password_entry.place(x=screen_width/2, y=screen_height/4 + 30)

tk.Label(root, text="Email:").place(x=screen_width/3, y=screen_height/4 + 60)
email_entry = tk.Entry(root)
email_entry.place(x=screen_width/2, y=screen_height/4 + 60)

tk.Label(root, text="Mobile Number:").place(x=screen_width/3, y=screen_height/4 + 90)
mobile_entry = tk.Entry(root)
mobile_entry.place(x=screen_width/2, y=screen_height/4 + 90)

# Create and place Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.place(x=screen_width/2, y=screen_height/4 + 120)

# Create labels and entry fields for login
tk.Label(root, text="Username:").place(x=screen_width/3, y=screen_height/2)
login_username_entry = tk.Entry(root)
login_username_entry.place(x=screen_width/2, y=screen_height/2)

tk.Label(root, text="Password:").place(x=screen_width/3, y=screen_height/2 + 30)
login_password_entry = tk.Entry(root, show="*")
login_password_entry.place(x=screen_width/2, y=screen_height/2 + 30)

# Create and place Login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.place(x=screen_width/2, y=screen_height/2 + 60)

root.mainloop()
