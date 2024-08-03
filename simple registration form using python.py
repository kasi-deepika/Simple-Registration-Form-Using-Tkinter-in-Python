import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name or not email or not age:
        messagebox.showwarning("Validation Error", "All fields are required")
    elif not age.isdigit():
        messagebox.showwarning("Validation Error", "Age must be a number")
    else:
        # Here you can add code to handle the form data, like storing it in a database
        messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x200")

# Create and place the labels and entry widgets for the form
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
