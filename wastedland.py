# Wastedland game
# (C)Wells & Aubrey 2020, All rights reserved

import os
import random
import time
import pygame as pg
from pygame.locals import *

from Assets.subtitles import openning
from Assets.assets import teammembers, enemies, weapons
title_interval = 5
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pg.pygame.init()
pg.font.init()
game_display = pg.display.set_mode((800, 600))
pg.display.set_caption('Wasteland Adventure')


def subtitle(title, interval=title_interval, cls=False):
    if cls:
        os.system('cls')

    if type(title) is list:
        for i in title:
            subtitle(i, cls=True)
    else:
        print(title)

    time.sleep(interval)


def attack(a, b):
    if b['live'] > 0:
        b['live'] = b['live'] - a['attack']
        subtitle("%s attacked %s, hurt %s %d point to health. %s live point left %d." % (
            a['name'],
            b['name'],
            b['name'],
            a['attack'],
            b['name'],
            b['live']
        ))


def meetEnemy():
    newEnemy = random.choice(enemies)
    e = {
        "name": newEnemy['name'],
        "attack": newEnemy['attack'],
        'live': newEnemy['live'],
        'experience_gain': newEnemy['experience_gain']
    }
    subtitle("Pipi and Aubrey met %s......" % e['name'], cls=True)
    return e


def endOfBattle(enemy):
    if enemy['live'] <= 0:
        return True

    for i in teammembers:
        if i['live'] > 0:
            return False
    return True


def gameOver():
    for i in teammembers:
        if i['live'] > 0:
            return False
    subtitle("All team member has been killed...Game over.")
    return True


subtitle(openning)

while not gameOver():

    e = meetEnemy()

    # The begin of battle
    while not endOfBattle(e):
        enemyAttackFirst = random.choice([True, False])

        if enemyAttackFirst:
            target = random.choice(teammembers)
            attack(e, target)

            if target['live'] < 0:
                subtitle("%s killed by %s..." % (target['name'], e['name']))
        for member in teammembers:
            if member['live'] > 0:
                attack(member, e)
                subtitle("%s gaind %d experience point from the battle." %
                         (member['name'], e['experience_gain']))
                member['experience'] = member['experience'] + \
                    e['experience_gain']
                if (member['experience'] >= 100):
                    member['level'] = member['level'] + 1
                    subtitle("%s upgraded, now level %d." %
                             (member['name'], member['level']))
                    member['experience'] = 0
                if (e['live'] <= 0):
                    subtitle("%s killed by %s" %
                             (e['name'], member['name']))
