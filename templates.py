
CELL_SIZE = 20
WIDTH = CELL_SIZE * 60
HEIGHT = CELL_SIZE * 45
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

IS_ACTIVE = False
PREVIOUS_MOUSE_STATE = False
CELLS = {}


GLIDER = [
    (260, 220),
    (480, 180),
    (380, 220),
    (80, 220),
    (460, 180),
    (260, 240),
    (540, 140),
    (340, 240),
    (760, 200),
    (540, 260),
    (740, 200),
    (380, 240),
    (500, 240),
    (460, 220),
    (480, 220),
    (280, 200),
    (60, 240),
    (380, 260),
    (60, 220),
    (360, 280),
    (400, 240),
    (280, 280),
    (300, 180),
    (540, 160),
    (740, 180),
    (760, 180),
    (80, 240),
    (540, 240),
    (500, 160),
    (320, 180),
    (300, 300),
    (320, 300),
    (360, 200),
    (480, 200),
    (260, 260),
    (460, 200),
]
GLIDER = {key: WHITE for key in GLIDER}

TEMPLATES = {
    1: ('Glider Gun', GLIDER),
    # 2: ('template name', LIVE_CELLS_LIST),  # EXAMPLE
    # ...
}
