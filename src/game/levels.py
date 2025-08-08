class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.level_data = None
        self.current_level = None

    def load_level(self):
        # Load level data from a file or define it here
        self.level_data = f"Data for level {self.level_number}"
        self.current_level = self.level_data

    def reset_level(self):
        # Reset the level to its initial state
        self.current_level = self.level_data

    def get_current_level(self):
        return self.current_level

    def __str__(self):
        return f"Level {self.level_number}: {self.current_level}"