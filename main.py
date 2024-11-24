import tkinter as tk
from generator import random_password

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x180")
root.resizable(0, 0)


label = tk.Label(root, 
                 text="Enter the length of the password: ",
                 font=("Helvetica", 16),
                 fg="black",
                 padx=10,
                 pady=10)

label.pack()

entry = tk.Entry(root,
                 font=("Arial", 14),
                 fg="black",
                 bg="lightgrey")

entry.pack(pady=10)

def on_button_click():
    feedback_text = random_password(int(entry.get()))
    label.config(text=feedback_text)

button = tk.Button(root, 
                   text="Submit",
                   font=("Arial", 14),
                   fg="white",
                   bg="green", 
                   activebackground="lightgreen",
                   command=on_button_click)


button.pack(pady=20)

root.mainloop()