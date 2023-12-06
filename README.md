# Pygame Game of Life

A simple implementation of Conway's Game of Life using the Pygame library. This script allows you to interactively set and visualize the initial state of the cellular automaton, and observe how it evolves over time according to the rules of the Game of Life.

## Conway's Game of Life Rules
The Game of Life is governed by four simple rules:

1. **Underpopulation**: In a live cell, represented by the yellow cells, if it has fewer than two live neighbors, it will die.
2. **Survival**: A live cell with two or three live neighbors will remain alive.
3. **Overpopulation**: If a live cell has more than three live neighbors, it dies due to overcrowding.
4. **Reproduction**: A dead cell with exactly three live neighbors becomes alive.

With these rules, the simulation dynamically adjusts the state of cells, creating visually interesting patterns and behaviors.

## Features
- **Interactive Setup**: Click on cells to toggle their state (alive/dead).
- **Play/Pause**: Press the spacebar to toggle between play and pause modes.
- **Clear Board**: Press 'c' to clear the entire board.
- **Randomize Board**: Press 'g' to add a random configuration of alive cells to the board.
- **Adjust Grid**: The game automatically applies the Game of Life rules to evolve the state of the cells.

## How to Play
1. Click on cells to set their initial state.
2. Press the spacebar to start or pause the simulation.
3. Use 'c' to clear the board or 'g' to add a random configuration.
4. Close the window to exit the game.

## Requirements
- Python 3.x
- Pygame library (`pip install pygame`)

## Controls
- **Mouse Click**: Toggle cell state
- **Spacebar**: Toggle play/pause
- **'c' Key**: Clear the board
- **'g' Key**: Add random cells to the board
