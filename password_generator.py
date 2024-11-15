import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive.")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Creating the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")
root.config(bg="#f0f8ff")  # Soft blue background for a calming effect

# Title Label
label_title = tk.Label(root, text="Secure Password Generator", font=("Helvetica", 18, "bold"), fg="#4B0082", bg="#f0f8ff")
label_title.pack(pady=15)

# Description Label
label_desc = tk.Label(root, text="Generate a strong, random password of your desired length.", font=("Helvetica", 10), fg="#4B0082", bg="#f0f8ff")
label_desc.pack()

# Length Input Frame
frame_length = tk.Frame(root, bg="#f0f8ff")
frame_length.pack(pady=10)

label_length = tk.Label(frame_length, text="Password Length:", font=("Helvetica", 12), bg="#f0f8ff")
label_length.grid(row=0, column=0, padx=5)

entry_length = tk.Entry(frame_length, width=10, font=("Helvetica", 12))
entry_length.grid(row=0, column=1)

# Generate Button
button_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"), bg="#4B0082", fg="white", width=20)
button_generate.pack(pady=10)

# Display Generated Password Frame
frame_password = tk.Frame(root, bg="#f0f8ff")
frame_password.pack(pady=5)

label_password = tk.Label(frame_password, text="Generated Password:", font=("Helvetica", 12), bg="#f0f8ff")
label_password.grid(row=0, column=0)

entry_password = tk.Entry(frame_password, width=30, font=("Helvetica", 12), fg="#4B0082")
entry_password.grid(row=0, column=1)

# Copy to Clipboard Button
button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 10, "bold"), bg="#32CD32", fg="white", width=15)
button_copy.pack(pady=10)

# Footer Label
label_footer = tk.Label(root, text="Secure your online accounts with a strong password!", font=("Helvetica", 9), fg="#4B0082", bg="#f0f8ff")
label_footer.pack(pady=5)

# Run the application
root.mainloop()
