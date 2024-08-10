import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

root = tk.Tk()
root.title("Get Your Name")
root.minsize(300, 150)
style = Style(theme="minty")
root = style.master

label = tk.Label(root, text="please enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()


def on_button_click():
    if entry.get() == "":
        messagebox.showerror("Error", "Please enter your name")
        return
    progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress.pack()
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        root.after(10)
    
    name = entry.get()
    messagebox.showinfo("YourName", f"Your name is: {name}")
    root.destroy()

button = tk.Button(root, text="Enter", command=on_button_click)
button.pack()

root.mainloop()
