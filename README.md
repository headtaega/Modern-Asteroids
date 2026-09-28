# Modern-Asteroids

## Description

A classic Asteroids arcade game built with Python and Pygame with modern features added!

## Features

- Classic asteroid-breaking gameplay
- Player ship with rotation and movement controls
- Three powerup types:
  - **Shield**: Blocks one asteroid hit
  - **Rapid Fire**: Increased shooting speed for 2.5 seconds
  - **Invincibility**: Pass through asteroids for 2.5 seconds
- Progressive asteroid splitting
- Score tracking and event logging
- 60 FPS gameplay
- open-source
- nice background

## Requirements

- Python 3.13 or higher
- Pygame 2.6.1

## Installation

1. Clone the repository
```bash
git clone https://github.com/headtaega/Modern-Asteroids.git
cd Modern-Asteroids
```

2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install pygame
```

## Running the Game

```bash
python main.py
```

## Controls

- **A/D**: Rotate ship left/right
- **W/S**: Move forward/backward
- **SPACE**: Shoot

## Game Objects

- **Player**: Your controllable ship
- **Asteroids**: Break them into smaller pieces
- **Powerups**: Collect for temporary abilities
- **Shots**: Destroy asteroids

## Author

[headtaega](https://github.com/headtaega)

## License

MIT
