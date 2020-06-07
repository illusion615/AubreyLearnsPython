"""
Assets file to define the character's profile
"""
TEAMMEMBERS = [
    {
        "name": "Aubrey",
        "attack": 20,
        "live": 100,
        "level": 1,
        "experience": 0,
        "iconPath": 'Assets/Images/aubrey.png',
        "iconSize": (100, 100)
    },
    {
        "name": "Pipi",
        "attack": 10,
        "live": 75,
        "level": 1,
        "experience": 0,
        "iconPath": 'Assets/Images/pipi.png',
        "iconSize": (100, 100)
    }
]

LEVELS = [
    {'level': 1, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 2, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 3, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 4, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 5, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 6, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 7, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 8, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 9, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100},
    {'level': 10, 'attack_increase': 1.1, 'live_increase': 1.1, 'upgrade': 100}
]

ENEMIES = [
    {"name": "Dog", "attack": 5, "live": 10, "experience_gain": 10},
    {"name": "Tiger", "attack": 20, "live": 50, "experience_gain": 20},
    {"name": "Pirate with pistol", "attack": 10, "live": 30, "experience_gain": 30},
    {"name": "Pirate with machine gun", "attack": 50,
     "live": 150, "experience_gain": 50},
    {"name": "Pirate with fatboy nuke", "attack": 100,
     "live": 150, "experience_gain": 100}
]

WEAPONS = [
    {"name": "Knife", "attack": 15},
    {"name": "Pistol", "attack": 10},
    {"name": "Machine gun", "attack": 50},
    {"name": "Fatboy nuke", "attack": 100}
]

OPENNING_SUBTITLE = [
    'Presented by Wells & Aubrey, 2020',
    'Pipi and Aubrey are in 2077, they have one boy called Sean.',
    'One day nuclear war was begin, and they escaped to monkey vault 56.'
    'They lived happily with many good friends, like crocodile and hippo.',
    "One day , the vault overseer send Pipi and Aubrey go to wasteland for food.",
    "When they back to the vault they can't find Sean, ",
    "They'd been told that pirate once came to the vault and took Sean away....",
    "Pipi and Aubury start the journey to find their son in the wasteland..."
]
