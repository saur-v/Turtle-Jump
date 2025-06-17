# 🦕 Dino Jump Game

A simple yet addictive dinosaur jumping game inspired by Chrome's offline dinosaur game, built using Python's Turtle graphics library.

## 🎮 Game Description

Control a white dinosaur that must jump over obstacles to survive. The game features randomly sized obstacles that appear from the right side of the screen. Your goal is to avoid collision by timing your jumps perfectly!

## 🚀 Features

- **Simple Controls**: Use the Up arrow key to jump
- **Random Obstacles**: Obstacles appear in two different sizes for varied difficulty
- **Collision Detection**: Game ends when the dinosaur hits an obstacle
- **Smooth Animation**: Fluid jumping mechanics and obstacle movement
- **Minimalist Design**: Clean white-on-black aesthetic

## 🎯 How to Play

1. Run the game using `python main.py`
2. Press the **Up Arrow Key** to make the dinosaur jump
3. Avoid hitting the white rectangular obstacles
4. Try to survive as long as possible!

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes built-in with Python)

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dino-jump-game.git
   cd dino-jump-game
   ```

2. Run the main game file:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
dino-jump-game/
│
├── main.py              # Main game loop and initialization
├── dino.py              # Dino class with game mechanics
├── tempCodeRunnerFile.py # Temporary file (can be ignored)
└── README.md            # This file
```

## 🎮 Game Mechanics

- **Dinosaur**: White turtle positioned on the left side of the screen
- **Obstacles**: White rectangles of varying sizes moving from right to left
- **Jumping**: Controlled arc movement when Up key is pressed
- **Collision**: Game detects collision based on distance and obstacle position
- **Game Over**: Displays "Game over" message when collision occurs

## 🔧 Technical Details

### Classes and Methods

**Dinos Class:**
- `__init__()`: Initializes the dinosaur character
- `Scree()`: Sets up the game screen
- `resist()`: Creates obstacles with random sizes
- `resist_move()`: Moves obstacles from right to left
- `jump()`: Handles dinosaur jumping animation
- `game_over()`: Displays game over screen

### Game Loop
The main game loop handles:
- Obstacle movement and regeneration
- Key input listening
- Collision detection
- Game state management

## 🎨 Customization

You can easily customize the game by modifying:
- **Colors**: Change dinosaur and obstacle colors in the respective methods
- **Speed**: Adjust movement speed in `resist_move()` and `jump()` methods
- **Screen Size**: Modify dimensions in `Scree()` method
- **Obstacle Sizes**: Edit the size array in `resist()` method
- **Jump Height**: Adjust the jump animation parameters in `jump()` method

## 🐛 Known Issues

- Game continues to listen for key presses even after game over
- No scoring system implemented
- No restart functionality without rerunning the script

## 🚧 Future Enhancements

- [ ] Add scoring system
- [ ] Implement restart functionality
- [ ] Add sound effects
- [ ] Include increasing difficulty over time
- [ ] Add high score tracking
- [ ] Implement different obstacle types

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements. Some areas where contributions are welcome:
- Bug fixes
- New features
- Code optimization
- Documentation improvements


## 🙏 Acknowledgments

- Inspired by Google Chrome's offline dinosaur game
- Built with Python's built-in Turtle graphics library

---

**Enjoy the game and happy jumping! 🦕**
