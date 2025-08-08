# filepath: advanced-tkinter-game/src/main.py

import tkinter as tk
from game.engine import GameEngine
from ui.screens import ScreenManager

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tkinter Game")
        self.root.geometry("800x600")
        
        self.screen_manager = ScreenManager(self.root)
        self.game_engine = GameEngine(self.screen_manager)

    def run(self):
        self.game_engine.start()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    app.run()