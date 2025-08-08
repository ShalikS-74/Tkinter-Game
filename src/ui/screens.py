import tkinter as tk

class ScreenManager(tk.Frame):
    """Must inherit from tk.Frame to be a proper Tkinter widget"""
    def __init__(self, master):
        super().__init__(master)
        self.screens = {}

    def add_screen(self, name, frame):
        """Add a new screen to the manager"""
        self.screens[name] = frame
        frame.place(relwidth=1, relheight=1)

    def show_screen(self, name):
        """Show the named screen"""
        for screen_name, frame in self.screens.items():
            frame.lower()
        self.screens[name].lift()