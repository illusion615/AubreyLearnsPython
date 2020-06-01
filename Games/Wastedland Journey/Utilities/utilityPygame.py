import pygame as pg
from pygame.locals import *
teampos = (10, 10)


class utilPygame:
    _font = pg.font

    def __init__(self):
        pg.font.init()
        self._font = pg.font.SysFont('Arial', 18)
        return

    def msgbox(screen, text, font=_font, bordercolor=pg.color.Color("WHITE")):
        _surface = pg.Surface(
            (
                self._font.get_size()[0] + 20,
                self._font.get_size()[1] + 20))
        _surface.fill(pg.Color(BLACK))
        _surface.border(bordercolor)

        #msgbox = pg.draw.rect(_surface, color, _rect_pos, 4)
        blit_text(_surface, text, (_rect_pos[0] + 10, _rect_pos[1] + 10), font)

        screen.blit(_surface, ((_surface.get_size()[0] - font.get_size()[0]) / 2,
                               (_surfce.get_size()[1] - font.get_size()[1]) / 2))

    def subtitle(title, time_to_disapear=2, cls=False):
        if cls:
            game_display.fill(BLACK)

        if type(title) is list:
            for i in title:
                subtitle(i, title_interval, True)
                pg.display.update()
        else:
            print(title)
            title_size = font.size(title)[0]
            blit_text(game_display, title,
                      ((SCREEN_WIDTH-title_size)/2, SCREEN_HEIGHT/2), font)
        time.sleep(time_to_disapear)

    def blit_text(surface, text, pos, font, color=pg.Color('white')):
        # 2D array where each row is a list of words.
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.


class ScreenObject:
    _position = None
    _obj = None

    def __init__(self, obj, position):
        self._position = position
        self._obj = obj
        return

    def getPosition():
        return self._position

    def getObj():
        return self._obj


class Screen:
    _title_interval = 2
    _display = None
    _stack = []

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)

    def __init__(self, topLeftPos=(0, 0), screen_size=(1024, 768), backgroundColor=WHITE, border=0):
        pg.init()
        msgFont = pg.font.SysFont('Arial', 22)
        panelFont = pg.font.SysFont('Arial', 18)
        self._display = pg.display.set_mode((1024, 768))
        pg.display.set_caption('Wasteland Adventure')
        return

    def refreshDisplay(self):
        # Re-draw screen background and fill with given background color.
        pg.draw.rect(_display, backgroundColor,
                     (topLeftPos[0], topLeftPos[1], screen_size[0], screen_size[1]), border)

        # Blit objects in stack on the screen
        for i in self._stack:
            self._display.blit(i)

        # Update the display
        pg.display.update()

    def addDisplayObj(self, obj):
        self._stack.append(obj)

    def drawTopPanel():
        topPanel = pg.draw.rect(game_display, WHITE,
                                (10, 10, SCREEN_WIDTH - 20, 125), 4)
        posx = 20
        n = 0
        for i in teammembers:
            roleDes = "%s\nHealth:%d\nLevel:%d\nExperience:%d\nAttack:%d" % (
                i['name'],
                i['live'],
                i['level'],
                i['experience'],
                i['attack']
            )
            game_display.blit(
                pg.transform.scale(pg.image.load(
                    i['iconPath']), i['iconSize']),
                (20 + 400*n, 20)
            )
            text = blit_text(game_display, roleDes,
                             (20 + 400 * n+120, 20), topPanelFont)
            n = n+1

    def drawBackground():
        return
