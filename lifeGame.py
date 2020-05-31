"""
The Game of Life

The Rules of Life
1. Cells with 0 or 1 neighbours die of loneliness
2. Cells with 2 or 3 neighbours survive
3. Cells with 4 or more neighbours die of overcrowding
4. Cells with exactly 3 neighbours come back to life
"""
import random
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (105, 105, 105)

_screenSize = (1024, 768)
_cellBackgroundPosition = (0, 68, 1024, 700)
_cellSize = (6, 6)
_numberOfRows = _cellBackgroundPosition[3] // _cellSize[1]
_numberOfColumns = _cellBackgroundPosition[2] // _cellSize[0]
_cells = []
_totalLifes = 0
_round = 0
pygame.init()
DISPLAY = pygame.display.set_mode((_screenSize[0], _screenSize[1]))
FONT = pygame.font.SysFont('monospace', 18)
pygame.display.set_caption('Game of Life - by Wells')
clock = pygame.time.Clock()

# Init cells and set default value to random value of 0 or 1, 0 means empty and 1 means life exist


def resetCells(randomseeds=False):
    global _cells, _round
    _cells = []
    _round = 0
    for r in range(0, _numberOfRows):
        _row = []
        for c in range(0, _numberOfColumns):
            if randomseeds:
                _row.append(random.randint(0, 1))
            else:
                _row.append(0)
        _cells.append(_row)


def drawSeeds(templateId):
    if templateId == 1:
        # Template block
        _cells[10][10] = 1
        _cells[10][11] = 1
        _cells[11][10] = 1
        _cells[11][11] = 1
    elif templateId == 2:
        # Template Bee-hive
        _cells[10][21] = 1
        _cells[10][22] = 1
        _cells[11][20] = 1
        _cells[11][23] = 1
        _cells[12][21] = 1
        _cells[12][22] = 1
    elif templateId == 3:
        # Template Glider
        _cells[10][30] = 1
        _cells[11][31] = 1
        _cells[12][29] = 1
        _cells[12][30] = 1
        _cells[12][31] = 1
    elif templateId == 4:
        # Template Gosper Glider Gun
        _cells[5][1] = _cells[5][2] = 1
        _cells[6][1] = _cells[6][2] = 1

        _cells[3][13] = _cells[3][14] = 1
        _cells[4][12] = _cells[4][16] = 1
        _cells[5][11] = _cells[5][17] = 1
        _cells[6][11] = _cells[6][15] = _cells[6][17] = _cells[6][18] = 1
        _cells[7][11] = _cells[7][17] = 1
        _cells[8][12] = _cells[8][16] = 1
        _cells[9][13] = _cells[9][14] = 1

        _cells[1][25] = 1
        _cells[2][23] = _cells[2][25] = 1
        _cells[3][21] = _cells[3][22] = 1
        _cells[4][21] = _cells[4][22] = 1
        _cells[5][21] = _cells[5][22] = 1
        _cells[6][23] = _cells[6][25] = 1
        _cells[7][25] = 1

        _cells[3][35] = _cells[3][36] = 1
        _cells[4][35] = _cells[4][36] = 1
        pass


def showMsg(msg, line=1):

    _font_surface = FONT.render(msg, True, WHITE)
    DISPLAY.blit(_font_surface, (10, 18*line))

# Draw cell with status


def evolve():
    global _cells, _totalLifes, _round

    cellsCopy = []
    for i in _cells:
        r = []
        for j in i:
            r.append(j)
        cellsCopy.append(r)

    _totalLifes = 0
    _round += 1
    for r in range(0, _numberOfRows):
        for c in range(0, _numberOfColumns):
            neighbours = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i != r or j != c):
                        if i >= 0 and j >= 0 and i <= _numberOfRows-1 and j <= _numberOfColumns-1 and cellsCopy[i][j] == 1:
                            neighbours += 1

            # Rule for survive
            if _cells[r][c] == 1:
                if neighbours < 2 or neighbours > 3:  # loneliness
                    _cells[r][c] = 0
            else:
                if neighbours == 3:  # Birth
                    _cells[r][c] = 1

            if _cells[r][c] == 1:
                _totalLifes += 1


def drawCells():
    global _totalLifes
    _totalLifes = 0

    pygame.draw.rect(DISPLAY, BLACK, (0, 0, 1024, 67))
    # Draw row lines
    for i in range(0, len(_cells)+1):
        pygame.draw.aaline(
            DISPLAY,
            GREY,
            (0, 68 + i * _cellSize[1]), (1024, 68 + i * _cellSize[1]))

    for i in range(0, len(_cells[0])+1):
        pygame.draw.aaline(
            DISPLAY,
            GREY,
            (0+i*_cellSize[0], 68), (0+i*_cellSize[0], 768))

    for r in range(0, _numberOfRows):
        for c in range(0, _numberOfColumns):
            if _cells[r][c] == 0:
                cellColor = BLACK
            else:
                cellColor = WHITE
                _totalLifes += 1

            cellPosition = (
                c*_cellSize[0]+_cellBackgroundPosition[0]+2,
                r*_cellSize[1]+_cellBackgroundPosition[1]+2,
                _cellSize[0]-4,
                _cellSize[1]-4)
            pygame.draw.rect(DISPLAY, cellColor, cellPosition)
    return


resetCells()
_running = True
_keepEvolving = False


while _running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                _keepEvolving = not _keepEvolving
            if event.key == K_ESCAPE:
                _running = False
            if event.key == K_0:
                resetCells()
            if event.key == K_1:
                drawSeeds(1)
            if event.key == K_2:
                drawSeeds(2)
            if event.key == K_3:
                drawSeeds(3)
            if event.key == K_4:
                drawSeeds(4)
            if event.key == K_9:
                resetCells(True)
            if event.key == K_RIGHT:
                _keepEvolving = False
                evolve()

    if _keepEvolving:
        evolve()

    drawCells()
    showMsg("Generation:%d   Total space:%d   Live cells:%d" %
            (_round, _numberOfColumns * _numberOfRows, _totalLifes))
    showMsg("Keep evolving: %d" % _keepEvolving, line=2)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
