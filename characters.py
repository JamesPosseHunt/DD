from loadouts import *
import random

class Race:

    def __init__(self, name, health, strength, speed, precision, shields=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.precision = precision
        self.shields = shields


class Character:

    def __init__(self, name, level, race, background, current_loadout):
        self.name = name
        self.level = level
        self.race = race
        self.background = background
        self.current_loadout = current_loadout
    def cqc(self):
        if self.background == cqc:
            self.race.strength += random.randint(0, 6)
        

spartan = Race("Spartan", 15, 10, 10, 5, 20)
human = Race("Human", 10, 5, 5, 2)
elite = Race("Elite", 20, 12, 10, 4, 15)
brute = Race("Brute", 25, 20, 10, 2)
grunt = Race("Grunt", 10, 5, 2, 2)
jackal = Race("Jackal", 10, 5, 2, 8)
hunter = Race("Hunter", 30, 40, 7, 2)

cqc = "cqc"
engineer = "engineer"
