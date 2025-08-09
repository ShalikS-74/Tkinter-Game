# Advanced Tkinter Red Block Game

A challenging survival game inspired by the classic "Red Block Game".  
Move the red block with your mouse and avoid the blue blocks for as long as possible!

## Features

- **Difficulty Selection:** Easy, Medium, Hard, and Impossible modes.
- **Impossible Mode:** 5 blue rectangles and 2 blue squares, fast speed, 1 second of invincibility, and a large red block.
- **Invincibility:** Temporary invincibility at the start of each game (duration depends on difficulty), with a yellow border that blinks in the last seconds.
- **Dynamic Speed:** Blue blocks get faster as you survive longer, with intervals based on difficulty.
- **Mouse Controls:** Hold and drag the mouse to move the red block.
- **Bouncing Blue Blocks:** Blue squares and rectangles bounce off the borders and never get stuck.
- **Game Over & Restart:** The game automatically restarts after you lose.
- **Instructions & Credits:** Instructions and credits are shown in the UI.

## Difficulty Modes

| Mode        | Blue Blocks         | Red Block Size | Invincibility | Speed Increase Interval | Starting Speed | Notes                      |
|-------------|---------------------|---------------|---------------|------------------------|---------------|-------------------------------|
| Easy        | 3 (mix)             | Small         | 5 seconds     | 2.5 seconds            | 2             |                               |
| Medium      | 5 (mix)             | Small         | 5 seconds     | 2 seconds              | 2             |                               |
| Hard        | 5 (mix)             | Large         | 2 seconds     | 1.5 seconds            | 2             |Size of player block increased |
| Impossible  | 7 (mix)             | Large         | 1 second      | 1 second               | 4             | Most blocks are rectangles    |

## How to Play

1. **Choose a difficulty** from the starting screen.
2. **Hold and drag the mouse** inside the black play area to move the red block.
3. **Avoid touching any blue block** (square or rectangle).
4. **Survive as long as you can!** Your time is displayed at the top left.
5. The game restarts automatically after you lose.

## Inspired By

*Inspired by Red Block Game*

---

## Requirements

- Python 3.8+
- Tkinter (comes with standard Python installations)

## Run the Game

```sh
python src/main.py
```

---

## Repository

Feel free to fork, contribute, or suggest new features!
