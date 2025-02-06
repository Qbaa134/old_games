import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Ustawienia okna gry
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Kształty Tetromino
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

SHAPE_COLORS = [CYAN, YELLOW, BLUE, GREEN, RED, ORANGE, MAGENTA]

# Funkcje pomocnicze
def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

def draw_shape(shape, x_offset, y_offset, color):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, (x_offset + x * BLOCK_SIZE, y_offset + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def valid_move(board, shape, x_offset, y_offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x_offset + x < 0 or x_offset + x >= SCREEN_WIDTH // BLOCK_SIZE or y_offset + y >= SCREEN_HEIGHT // BLOCK_SIZE:
                    return False
                if board[y_offset + y][x_offset + x]:
                    return False
    return True

def clear_lines(board):
    full_lines = [i for i, row in enumerate(board) if all(row)]
    for i in full_lines:
        board.pop(i)
        board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
    return len(full_lines)

def draw_board(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, SHAPE_COLORS[cell - 1], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Funkcja rysująca napis wstępny
def draw_start_screen():
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Press Enter to Start", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Wyśrodkowanie tekstu
    screen.blit(text, text_rect)

# Funkcja pauzy
def draw_pause_screen():
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("Paused. Press Space to Resume", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Wyśrodkowanie tekstu
    screen.blit(text, text_rect)

# Główna funkcja gry
def game():
    board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    clock = pygame.time.Clock()
    game_over = False
    pause = False
    current_shape = random.choice(list(zip(SHAPES, SHAPE_COLORS)))
    shape, color = current_shape
    x_offset = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2
    y_offset = 0
    fall_speed = 0.2  # Zwalnianie spadania (im większa wartość, tym wolniej)

    # Ekran początkowy
    while not game_over:
        screen.fill(BLACK)
        draw_start_screen()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Rozpoczęcie gry po naciśnięciu Enter
                    game_loop()

# Pętla gry
def game_loop():
    board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    clock = pygame.time.Clock()
    game_over = False
    pause = False
    current_shape = random.choice(list(zip(SHAPES, SHAPE_COLORS)))
    shape, color = current_shape
    x_offset = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2
    y_offset = 0
    fall_time = 0  # Czas spadania
    fall_speed = 0.01  # Zwalnianie spadania (im większa wartość, tym wolniej)

    while not game_over:
        screen.fill(BLACK)
        draw_grid()
        draw_board(board)
        draw_shape(shape, x_offset * BLOCK_SIZE, y_offset * BLOCK_SIZE, color)

        if pause:
            draw_pause_screen()
            pygame.display.flip()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_move(board, shape, x_offset - 1, y_offset):
                        x_offset -= 1
                elif event.key == pygame.K_RIGHT:
                    if valid_move(board, shape, x_offset + 1, y_offset):
                        x_offset += 1
                elif event.key == pygame.K_DOWN:
                    if valid_move(board, shape, x_offset, y_offset + 1):
                        y_offset += 1
                elif event.key == pygame.K_UP:
                    rotated_shape = rotate_shape(shape)
                    if valid_move(board, rotated_shape, x_offset, y_offset):
                        shape = rotated_shape
                elif event.key == pygame.K_SPACE:  # Pauza po spacji
                    pause = not pause

        if not pause:
            fall_time += clock.get_rawtime() / 1000.0
            if fall_time >= fall_speed:
                if valid_move(board, shape, x_offset, y_offset + 1):
                    y_offset += 1
                else:
                    for y, row in enumerate(shape):
                        for x, cell in enumerate(row):
                            if cell:
                                board[y_offset + y][x_offset + x] = SHAPE_COLORS.index(color) + 1
                    cleared = clear_lines(board)
                    current_shape = random.choice(list(zip(SHAPES, SHAPE_COLORS)))
                    shape, color = current_shape
                    x_offset = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2
                    y_offset = 0
                    if not valid_move(board, shape, x_offset, y_offset):
                        game_over = True
                fall_time = 0  # Resetowanie czasu spadania

        pygame.display.flip()
        clock.tick(30)  # Zwiększ lub zmniejsz wartość, aby kontrolować prędkość gry

    pygame.quit()

if __name__ == "__main__":
    game()

