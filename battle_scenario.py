from arpg_mechanics import ARPGMechanics


class Bow:
    def __init__(self, crit_chance, max_frenzy, bow_speed):
        self.crit_chance = crit_chance
        self.max_frenzy = max_frenzy
        self.bow_speed = bow_speed

class Enemy:
    def __init__(self, position, size):
        self.position = position
        self.size = size
