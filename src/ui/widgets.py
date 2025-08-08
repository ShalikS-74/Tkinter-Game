import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(font=("Arial", 12), bg="lightblue", activebackground="blue", padx=10, pady=5)

class CustomLabel(tk.Label):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.config(font=("Arial", 14), bg="white", fg="black")

class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Arial", 12), bg="lightgrey", fg="black", padx=5)

class CustomFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="white")