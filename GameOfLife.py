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
HINT = "1:Block   2:Beehive   3:Glider   4:Gosper Glider Gun   9:Random Seed   0:Reset"
HINT2 = "ESC: Quit   -:Zoom out   =:Zoom out   Space:Turn on/off continually evolving   Right:Step evolving"
_screenSize = (1024, 768)
_topPanelHeight = _bottomPanelHeight = 77
_cellBackgroundPosition = (
    0, _topPanelHeight+1, _screenSize[0], _screenSize[1]-2*_topPanelHeight)
_cellSize = 10
_numberOfRows = _cellBackgroundPosition[3] // _cellSize
_numberOfColumns = _cellBackgroundPosition[2] // _cellSize
_cells = []
_totalLifes = 0
_generations = 0
_running = True
_keepEvolving = False
_stablized = 0

pygame.init()
DISPLAY = pygame.display.set_mode((_screenSize[0], _screenSize[1]))
FONT = pygame.font.SysFont('arial', 18)
pygame.display.set_caption('Game of Life - by Wells')
clock = pygame.time.Clock()


def resetCells(randomseeds=False):
    """
    Init cells and set default value to random value of 0 or 1, 0 means empty and 1 means life exist
    """
    global _cells, _generations, _numberOfRows, _numberOfColumns, _stablized
    _stablized = 0
    _numberOfRows = _cellBackgroundPosition[3] // _cellSize
    _numberOfColumns = _cellBackgroundPosition[2] // _cellSize
    _cells = []
    _generations = 0
    for r in range(0, _numberOfRows):
        _row = []
        for c in range(0, _numberOfColumns):
            if randomseeds:
                _row.append(random.randint(0, 2))
            else:
                _row.append(0)
        _cells.append(_row)


def drawSeeds(templateId):
    """
    Draw buit-in seed template
    """
    if templateId == 1:
        # Template block
        _cells[10][10] = _cells[10][11] = 1
        _cells[11][10] = _cells[11][11] = 1
    elif templateId == 2:
        # Template Bee-hive
        _cells[10][21] = _cells[10][22] = 1
        _cells[11][20] = _cells[11][23] = 1
        _cells[12][21] = _cells[12][22] = 1
    elif templateId == 3:
        # Template Glider
        _cells[10][30] = 1
        _cells[11][31] = 1
        _cells[12][29] = _cells[12][30] = _cells[12][31] = 1
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


def showMsg(msg, line=1, top=True):

    _font_surface = FONT.render(msg, True, WHITE)
    if top:
        fontPos = (10, 18 * line)
    else:
        fontPos = (10, 18*line+_screenSize[1]-_bottomPanelHeight)
    DISPLAY.blit(_font_surface, fontPos)


def evolve(pauseWhenStablized=True):
    global _cells, _totalLifes, _generations, _stablized
    if pauseWhenStablized and _stablized == 10:
        return

    survived = 0
    cellsCopy = []
    for i in _cells:
        r = []
        for j in i:
            r.append(j)
        cellsCopy.append(r)

    _generations += 1
    for r in range(0, len(_cells)):
        for c in range(0, len(_cells[r])):
            neighbours = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i != r or j != c):
                        if i >= 0 and j >= 0 and i < len(_cells) and j < len(_cells[0]) and cellsCopy[i][j] == 1:
                            neighbours += 1

            # Rule for survive
            if _cells[r][c] == 1:
                if neighbours < 2 or neighbours > 3:  # loneliness
                    _cells[r][c] = 0
            else:
                if neighbours == 3:  # Birth
                    _cells[r][c] = 1

            if _cells[r][c] == 1:
                survived += 1

    if survived == _totalLifes:
        _stablized += 1
    else:
        _stablized = 0

    _totalLifes = survived


def drawCells():
    """
    Draw cell with status
    """
    global _totalLifes, _numberOfColumns, _numberOfRows

    _totalLifes = 0
    DISPLAY.fill(BLACK)  # Fill background color to BLACK

    # Draw top panel for display text
    pygame.draw.rect(DISPLAY, BLACK, (0, 0, _screenSize[0], _topPanelHeight))
    # Draw bottom panel for display text
    pygame.draw.rect(
        DISPLAY, BLACK, (0, 0, _screenSize[0], _screenSize[1]-_bottomPanelHeight))
    # Draw row lines
    for i in range(0, _numberOfRows+1):
        pygame.draw.aaline(
            DISPLAY,
            GREY,
            (0, _topPanelHeight + i*_cellSize), (_screenSize[0], _topPanelHeight + i*_cellSize))
    # Draw column lines
    for i in range(0, _numberOfColumns+1):
        pygame.draw.aaline(
            DISPLAY,
            GREY,
            (i*_cellSize, _topPanelHeight), (i*_cellSize, _topPanelHeight+_numberOfRows*_cellSize))

    for r in range(0, _numberOfRows):
        for c in range(0, _numberOfColumns):
            if _cells[r][c] == 0:
                cellColor = BLACK
            else:
                cellColor = WHITE
                _totalLifes += 1

            cellPosition = (
                c*_cellSize+_cellBackgroundPosition[0]+2,
                r*_cellSize+_cellBackgroundPosition[1]+2,
                _cellSize-4,
                _cellSize-4)
            pygame.draw.rect(DISPLAY, cellColor, cellPosition)
    return


def recalculateCellsSize():
    global _numberOfColumns, _numberOfRows
    _numberOfRows = _cellBackgroundPosition[3] // _cellSize
    _numberOfColumns = _cellBackgroundPosition[2] // _cellSize

    for i in _cells:
        for j in range(len(i), _numberOfColumns):
            i.append(0)
    for i in range(len(_cells), _numberOfRows):
        t = []
        for j in range(0, len(_cells[0])):
            t.append(0)
        _cells.append(t)


# Main entry
resetCells()

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
                evolve(pauseWhenStablized=False)
            if event.key == K_MINUS:
                _cellSize -= 1
                if _cellSize < 1:
                    _cellSize = 1
                recalculateCellsSize()
            if event.key == K_EQUALS:
                _cellSize += 1

    if _keepEvolving:
        evolve()

    drawCells()
    showMsg("Generation:%d    Cellulars survived:%d" %
            (_generations, _totalLifes))
    showMsg("Continually evolving:%r    Cellular size:%d    Total spaces:%d" %
            (_keepEvolving, _cellSize, _numberOfColumns * _numberOfRows), line=2)
    showMsg(HINT, top=False)
    showMsg(HINT2, line=2, top=False)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
