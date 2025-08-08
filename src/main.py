import tkinter as tk
from ui.screens import ScreenManager
from game.engine import GameEngine

class GameApp:
    def __init__(self, root):
        self.root = root
        self.enemy_count = 3  # Default
        self.setup_game()

    def setup_game(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        self.screen_manager = ScreenManager(self.main_frame)
        self.screen_manager.pack(fill='both', expand=True)

        # Difficulty selection screen
        difficulty_screen = tk.Frame(self.screen_manager, bg="white")
        label = tk.Label(difficulty_screen, text="Choose Difficulty", font=("Arial", 16), bg="white", fg="black")
        label.pack(pady=20)

        easy_btn = tk.Button(difficulty_screen, text="Easy (3 blue blocks)", font=("Arial", 12),
                             command=lambda: self.start_game(3))
        easy_btn.pack(pady=10)

        medium_btn = tk.Button(difficulty_screen, text="Medium (5 blue blocks)", font=("Arial", 12),
                               command=lambda: self.start_game(5))
        medium_btn.pack(pady=10)

        self.screen_manager.add_screen("difficulty", difficulty_screen)

        # Game screen setup (created when starting game)
        self.screen_manager.show_screen("difficulty")

    def start_game(self, enemy_count):
        difficulty = "medium" if enemy_count == 5 else "easy"
        self.enemy_count = enemy_count
        # Remove previous game screen if exists
        if hasattr(self, 'game_screen'):
            self.game_screen.destroy()
        self.game_screen = tk.Frame(self.screen_manager)
        canvas = tk.Canvas(self.game_screen, width=400, height=300, bg="white", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(0, 0, 400, 300, fill="black", outline="black")
        instructions = tk.Label(
            self.game_screen,
            text="Instructions:\nMove the red block by holding and dragging the mouse.\nAvoid touching any blue block. Survive as long as you can!",
            font=("Arial", 12),
            fg="black",
            bg="white",
            justify="center"
        )
        instructions.pack(pady=10)
        self.screen_manager.add_screen("game", self.game_screen)
        self.screen_manager.show_screen("game")
        self.game_engine = GameEngine(canvas, enemy_count, difficulty)
        self.game_engine.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = GameApp(root)
    root.mainloop()