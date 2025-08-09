import tkinter as tk
from ui.screens import ScreenManager
from game.engine import GameEngine

class GameApp:
    def __init__(self, root):
        self.root = root
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

        # Impossible button at the top
        impossible_btn = tk.Button(difficulty_screen, text="Impossible (8 rectangles, fast, 1s invincibility)", font=("Arial", 12, "bold"),
                                   fg="red",
                                   command=lambda: self.start_game(8, "impossible"))
        impossible_btn.pack(pady=10)

        easy_btn = tk.Button(difficulty_screen, text="Easy (3 blue blocks)", font=("Arial", 12),
                             command=lambda: self.start_game(3, "easy"))
        easy_btn.pack(pady=10)

        medium_btn = tk.Button(difficulty_screen, text="Medium (5 blue blocks)", font=("Arial", 12),
                               command=lambda: self.start_game(5, "medium"))
        medium_btn.pack(pady=10)

        hard_btn = tk.Button(difficulty_screen, text="Hard (5 blue blocks, big red block)", font=("Arial", 12),
                             command=lambda: self.start_game(5, "hard"))
        hard_btn.pack(pady=10)

        # Inspired by Red Block Game label
        inspired_label = tk.Label(
            difficulty_screen,
            text="Inspired by Red Block Game",
            font=("Arial", 9, "italic"),
            fg="gray",
            bg="white"
        )
        inspired_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.screen_manager.add_screen("difficulty", difficulty_screen)
        self.screen_manager.show_screen("difficulty")

    def start_game(self, enemy_count, difficulty):
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