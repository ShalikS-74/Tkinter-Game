# test_validation.py
import tkinter as tk
from main import GameApp

def test_root_window():
    root = tk.Tk()
    try:
        app = GameApp(root)
        print("✓ Root window validation passed")
        return True
    except Exception as e:
        print(f"✗ Root window validation failed: {e}")
        return False

if __name__ == "__main__":
    test_root_window()