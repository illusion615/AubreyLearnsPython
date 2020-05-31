# Wastedland game
# (C)Wells & Aubrey 2020, All rights reserved

import os
import random
import time

from Utilities.utilityGame import *
from Utilities.utilityPygame import *

from Assets.subtitles import openning
from Assets.assets import teammembers, enemies, weapons

screenStart = Screen()
# screenStart.addDisplayObj()
# The beginning of the game, display title.
subtitle(openning)

running = True
while running:

    game_display.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == pg.K_LEFT:
                teampos[0] -= 1
            if event.key == pg.K_RIGHT:
                teampos[0] += 1
            if event.key == pg.K_UP:
                teampos[1] -= 1
            if event.key == pg.K_DOWN:
                teampos[1] += 1

    if gameOver():
        quit()

    e = meetEnemy()

    # The begin of battle
    while not endOfBattle(e):
        game_display.fill(BLACK)

        drawTopPanel()
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
                    member['level'] += 1
                    member['attack'] *= 1.1
                    member['live'] = member['live']*1.1
                    subtitle("%s upgraded, now level %d." %
                             (member['name'], member['level']))
                    member['experience'] = 0
                if (e['live'] <= 0):
                    subtitle("%s killed by %s" %
                             (e['name'], member['name']))
            refreshDisplay()

        refreshDisplay()
