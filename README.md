# 🐍 Snake Game

A modern implementation of the classic Snake Game built with **Python** and **Pygame**.  
This project demonstrates clean modular design, configurable settings, and extended features such as difficulty levels, theming, sound effects, and game state persistence.

---

## ✨ Key Features
- **Classic gameplay** – smooth grid-based snake mechanics.  
- **Configurable difficulty** – Easy, Normal, and Hard modes.  
- **Custom themes** – multiple snake color palettes and backgrounds.  
- **Audio feedback** – sound effects for movement, collisions, and game events.  
- **Pause & resume** – intuitive in-game pause system.  
- **Persistent state** – continue previous sessions using the save system.  

---

## 📂 Project Structure
```bash
snake-game/
├── main.py            # Entry point, menu, and settings
├── game.py            # Core gameplay loop
├── setting.py         # Configurations and asset loading
├── continueGame.py    # Save/load game state
├── character.py       # Snake and fruit implementations
├── color.py           # Color constants
├── data/              # Save data (snake, fruit, score, etc.)
├── images/            # UI and sprite assets
└── sounds/            # Sound effects
```
---
## 🔧 Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.8+** → [Download here](https://www.python.org/downloads/)  
- **Pygame** → for game graphics and input handling  
- **NumPy** → for mathematical operations used in the game  
