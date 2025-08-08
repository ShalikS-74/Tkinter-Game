class ScreenManager:
    def __init__(self, master):
        self.master = master
        self.screens = {}

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def show_screen(self, name):
        for screen in self.screens.values():
            screen.pack_forget()
        self.screens[name].pack(fill='both', expand=True)

    def hide_screen(self, name):
        if name in self.screens:
            self.screens[name].pack_forget()