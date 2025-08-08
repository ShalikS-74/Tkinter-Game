import tkinter as tk
import random
import time

class GameEngine:
    def __init__(self, canvas, enemy_count=3, difficulty="easy"):
        self.canvas = canvas
        self.enemy_size = 50
        self.enemy_count = enemy_count
        self.difficulty = difficulty
        self.running = False
        self.mouse_down = False
        self.canvas_width = 400
        self.canvas_height = 300
        self.player_size = 30
        self.player_pos = [180, 130]
        canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        canvas.bind("<Motion>", self.on_mouse_move)
        self.spawn_enemies(5)

    def start(self):
        self.canvas.delete("all")
        self.player_pos = [180, 130]
        self.spawn_enemies(self.enemy_count)
        self.player = self.canvas.create_rectangle(
            self.player_pos[0], self.player_pos[1],
            self.player_pos[0] + self.player_size, self.player_pos[1] + self.player_size,
            fill="red"
        )
        self.survival_text = self.canvas.create_text(
            70, 20, text="Time: 0.00s", fill="black", font=("Arial", 16)
        )
        self.start_time = time.time()
        self.running = True
        self.enemy_speed = 2
        self.game_loop()

    def spawn_enemies(self, count):
        self.enemies = []
        self.enemy_dirs = []
        min_distance = 80  # Minimum distance from red block
        for _ in range(count):
            shape = random.choice(["rectangle", "square"])
            if shape == "rectangle":
                max_x = self.canvas_width - self.enemy_size
                max_y = self.canvas_height - self.enemy_size * 2  # Rectangle is taller
            else:
                max_x = self.canvas_width - self.enemy_size
                max_y = self.canvas_height - self.enemy_size
            while True:
                x = random.randint(0, max_x)
                y = random.randint(0, max_y)
                px = self.player_pos[0] + self.player_size / 2
                py = self.player_pos[1] + self.player_size / 2
                ex = x + self.enemy_size / 2
                ey = y + (self.enemy_size if shape == "square" else self.enemy_size)
                distance = ((px - ex) ** 2 + (py - ey) ** 2) ** 0.5
                if distance > min_distance:
                    break
            if shape == "rectangle":
                enemy = self.canvas.create_rectangle(
                    x, y, x + self.enemy_size, y + self.enemy_size * 2,
                    outline="blue", width=3, fill="blue"
                )
            else:
                enemy = self.canvas.create_rectangle(
                    x, y, x + self.enemy_size, y + self.enemy_size,
                    outline="blue", width=3, fill="blue"
                )
            self.enemies.append(enemy)
            self.enemy_dirs.append([random.choice([-1, 1]), random.choice([-1, 1])])

    def on_mouse_down(self, event):
        self.mouse_down = True

    def on_mouse_up(self, event):
        self.mouse_down = False

    def on_mouse_move(self, event):
        if not self.running or not self.mouse_down:
            return
        # Center the player on the mouse cursor, keep inside black area
        x = max(0, min(event.x - self.player_size // 2, self.canvas_width - self.player_size))
        y = max(0, min(event.y - self.player_size // 2, self.canvas_height - self.player_size))
        self.player_pos = [x, y]
        self.canvas.coords(
            self.player,
            self.player_pos[0], self.player_pos[1],
            self.player_pos[0] + self.player_size, self.player_pos[1] + self.player_size
        )

    def game_loop(self):
        if not self.running:
            return
        self.move_enemies_random()
        self.update_time()
        self.increase_difficulty()
        # Prevent death in first 5 seconds
        if self.survival_time >= 5 and self.check_collision():
            self.game_over()
            return
        self.canvas.after(50, self.game_loop)

    def move_enemies_random(self):
        for idx, enemy in enumerate(self.enemies):
            ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
            dx, dy = self.enemy_dirs[idx]
            # Calculate new position
            new_x1 = ex1 + dx * self.enemy_speed
            new_y1 = ey1 + dy * self.enemy_speed
            new_x2 = ex2 + dx * self.enemy_speed
            new_y2 = ey2 + dy * self.enemy_speed

            # Bounce off left/right walls
            if new_x1 < 0 or new_x2 > self.canvas_width:
                self.enemy_dirs[idx][0] *= -1
                dx = self.enemy_dirs[idx][0]
            # Bounce off top/bottom walls
            if new_y1 < 0 or new_y2 > self.canvas_height:
                self.enemy_dirs[idx][1] *= -1
                dy = self.enemy_dirs[idx][1]
            # Occasionally change direction randomly
            if random.random() < 0.05:
                self.enemy_dirs[idx] = [random.choice([-1, 1]), random.choice([-1, 1])]
                dx, dy = self.enemy_dirs[idx]
            # Move enemy
            self.canvas.move(enemy, dx * self.enemy_speed, dy * self.enemy_speed)

    def check_collision(self):
        px1, py1 = self.player_pos
        px2, py2 = px1 + self.player_size, py1 + self.player_size
        for enemy in self.enemies:
            ex1, ey1, ex2, ey2 = self.canvas.coords(enemy)
            if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
                return True
        return False

    def update_time(self):
        self.survival_time = time.time() - self.start_time
        self.canvas.itemconfig(self.survival_text, text=f"Time: {self.survival_time:.2f}s", fill="black")

    def increase_difficulty(self):
        # Easy: every 2.5 seconds, Medium: every 2 seconds
        interval = 2 if self.difficulty == "medium" else 2.5
        self.enemy_speed = 2 + int(self.survival_time // interval)

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            self.canvas_width // 2, self.canvas_height // 2,
            text=f"Game Over!\nSurvived: {self.survival_time:.2f}s",
            fill="black", font=("Arial", 24)
        )
        self.canvas.after(2000, self.reset_game)

    def reset_game(self):
        self.start()  # Do NOT increase enemy_count