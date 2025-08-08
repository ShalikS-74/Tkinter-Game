from playsound import playsound
import os

class SoundManager:
    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, filepath):
        if os.path.exists(filepath):
            self.sounds[name] = filepath
        else:
            print(f"Sound file {filepath} not found.")

    def play_sound(self, name):
        if name in self.sounds:
            playsound(self.sounds[name])
        else:
            print(f"Sound {name} not loaded.")

    def stop_sound(self, name):
        # Placeholder for stopping sound functionality
        pass

    def load_all_sounds(self):
        # Load all sounds here if needed
        pass

# Example usage
if __name__ == "__main__":
    sound_manager = SoundManager()
    sound_manager.load_sound("jump", "assets/sounds/jump.wav")
    sound_manager.play_sound("jump")