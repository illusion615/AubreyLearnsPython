# Utility glass for battle system
from Assets.assets import teammembers, enemies, weapons


def attack(a, b):
    if b['live'] > 0:
        b['live'] = b['live'] - a['attack']
        drawTopPanel()
        subtitle("%s attacked %s, hurt %s %d point to health. %s live point left %d." % (
            a['name'],
            b['name'],
            b['name'],
            a['attack'],
            b['name'],
            b['live']
        ))
        pg.display.update()


def endOfBattle(enemy):
    if enemy['live'] <= 0:
        return True

    for i in teammembers:
        if i['live'] > 0:
            return False
    return True


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


def gameOver():
    for i in teammembers:
        if i['live'] > 0:
            return False
    subtitle("All team member has been killed...Game over.")
    return True
