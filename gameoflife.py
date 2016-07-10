#!/usr/bin/env python

import logging
import pygame
import random
import sys
from time import sleep

from templates import *


pygame.init()
screen = pygame.display.set_mode(SIZE)


def generate_board(clear=False, tpl=None):
    for x in xrange(0, WIDTH, CELL_SIZE):
        for y in xrange(0, HEIGHT, CELL_SIZE):
            color = random.choice((BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WHITE))
            CELLS[(x, y)] = BLACK if clear or tpl else color

    if tpl:
        CELLS.update(tpl)


def get_neighbours(cell):
    neighbours = []

    for ny in  xrange(-1, 2):
        for nx in xrange(-1, 2):
            x, y = tuple(sum(x) for x in zip(cell, (nx * CELL_SIZE, ny * CELL_SIZE)))

            if x < 0:
                x = WIDTH - CELL_SIZE
            if y < 0:
                y = HEIGHT - CELL_SIZE

            new_cell = (x, y)
            if new_cell != cell:
                neighbours.append(new_cell)

    return neighbours


def draw_help():
    font = pygame.font.SysFont("monospace", 20)
    font.set_bold(True)
    label = font.render("S - start/stop, Q - quit", 1, (200, 0, 0), BLACK)
    screen.blit(label, (10, 10))
    label = font.render("R - restart, C - clear, P - print current state", 1, (200, 0, 0), BLACK)
    screen.blit(label, (10, 30))


    label = font.render("Templates: 1 - Glider Gun", 1, (200, 0, 0), BLACK)
    screen.blit(label, (10, HEIGHT - 30))


def cursor_draw():
    mouse_state = pygame.mouse.get_pressed() != (0, 0, 0)
    global PREVIOUS_MOUSE_STATE

    if not PREVIOUS_MOUSE_STATE and mouse_state:
        cursor_pos = pygame.mouse.get_pos()
        cell_pos = tuple(map(lambda p: p / CELL_SIZE * CELL_SIZE, cursor_pos))
        if CELLS.get(cell_pos, WHITE) == WHITE:
            CELLS[cell_pos] = BLACK
        else:
            CELLS[cell_pos] = WHITE

    PREVIOUS_MOUSE_STATE = mouse_state


def update_cells():
    '''
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by over-population.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''

    new_states = {}
    for cell, color in CELLS.items():
        pygame.draw.rect(
            screen,
            color,
            [cell[0], cell[1], CELL_SIZE, CELL_SIZE],
        )

        if IS_ACTIVE:
            live_cells = 0
            for neighbour in get_neighbours(cell):
                live_cells += 1 if CELLS.get(neighbour, BLACK) == WHITE else 0

            new_state = CELLS[cell]
            if CELLS[cell] == WHITE:
                if live_cells < 2:
                    new_state = BLACK
                if live_cells in (2, 3):
                    new_state = WHITE
                if live_cells > 3:
                    new_state = BLACK
            else:
                if live_cells == 3:
                    new_state = WHITE

            new_states[cell] = new_state

    CELLS.update(new_states)


def run():
    generate_board()

    global IS_ACTIVE

    while 1:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    IS_ACTIVE = not IS_ACTIVE
                if event.key == pygame.K_r:
                    generate_board()
                if event.key == pygame.K_c:
                    generate_board(True)
                if event.key == pygame.K_1:
                    generate_board(True, TEMPLATES[1])
                if event.key == pygame.K_q:
                    sys.exit()

                if event.key == pygame.K_p:
                    print [key for key, value in CELLS.items() if value == WHITE]

        cursor_draw()
        update_cells()
        draw_help()
        pygame.display.flip()


if __name__ == "__main__":
    run()
