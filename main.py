import pygame
import random

class GameOfLife:
    def __init__(self):
        # Initialize game parameters
        self.width = 800
        self.height = 800
        self.tile_size = 20
        self.grid_width = self.width // self.tile_size
        self.grid_height = self.height // self.tile_size
        self.fps = 60

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Paused")

        self.clock = pygame.time.Clock()

        # Initialize game state
        self.running = True
        self.playing = False
        self.count = 0
        self.update_freq = 120

        self.positions = set()

    def gen(self, num):
        # Generate a set of random positions
        return set([(random.randrange(0, self.grid_height), random.randrange(0, self.grid_width)) for _ in range(num)])

    def draw_grid(self):
        # Draw the grid on the screen
        self.screen.fill((128, 128, 128))

        # Draw alive cells
        for position in self.positions:
            col, row = position
            top_left = (col * self.tile_size, row * self.tile_size)
            pygame.draw.rect(self.screen, (255, 255, 0), (*top_left, self.tile_size, self.tile_size))

        # Draw grid lines
        for row in range(self.grid_height):
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * self.tile_size), (self.width, row * self.tile_size))

        for col in range(self.grid_width):
            pygame.draw.line(self.screen, (0, 0, 0), (col * self.tile_size, 0), (col * self.tile_size, self.height))

    def adjust_grid(self):
        # Adjust the grid based on the Game of Life rules
        all_neighbors = set()
        new_positions = set()

        for position in self.positions:
            neighbors = self.get_neighbors(position)
            all_neighbors.update(neighbors)

            neighbors = list(filter(lambda x: x in self.positions, neighbors))

            if len(neighbors) in [2, 3]:
                new_positions.add(position)

        for position in all_neighbors:
            neighbors = self.get_neighbors(position)
            neighbors = list(filter(lambda x: x in self.positions, neighbors))

            if len(neighbors) == 3:
                new_positions.add(position)

        self.positions = new_positions

    def get_neighbors(self, pos):
        # Get neighbors of a given position
        x, y = pos
        neighbors = []

        for dx in [-1, 0, 1]:
            if 0 <= x + dx < self.grid_width:
                for dy in [-1, 0, 1]:
                    if 0 <= y + dy < self.grid_height and not (dx == 0 and dy == 0):
                        neighbors.append((x + dx, y + dy))

        return neighbors

    def handle_events(self):
        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle cell state on mouse click
                x, y = pygame.mouse.get_pos()
                col = x // self.tile_size
                row = y // self.tile_size
                pos = (col, row)

                if pos in self.positions:
                    self.positions.remove(pos)
                else:
                    self.positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle play/pause on spacebar press
                    self.playing = not self.playing

                if event.key == pygame.K_c:
                    # Clears the board when 'c' key is pressed
                    self.clear_board()

                if event.key == pygame.K_g:
                    # Add random tiles to the board when 'g' key is pressed
                    self.randomize_board()

    def clear_board(self):
        # Clear the game board
        self.positions = set()
        self.playing = False
        self.count = 0

    def randomize_board(self):
        # Add random tiles to the game board
        self.positions = self.gen(random.randrange(2, 5) * self.grid_width)

    def run(self):
        # Main game loop
        while self.running:
            self.clock.tick(self.fps)

            if self.playing:
                self.count += 1

            if self.count >= self.update_freq:
                self.count = 0
                self.adjust_grid()

            pygame.display.set_caption("Playing" if self.playing else "Paused")

            self.handle_events()

            self.draw_grid()

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    # Run the GameOfLife class when the script is executed
    game = GameOfLife()
    game.run()