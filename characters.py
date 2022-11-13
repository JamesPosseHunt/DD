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
        self.tech = 1


class Character:

    def __init__(self, name, level, race, background, current_loadout):
        self.name = name
        self.level = level
        self.race = race
        self.background = background
        self.current_loadout = current_loadout
        if self.race == "Spartan":
            self.race = spartan
        elif self.race == "Human":
            self.race = human
        elif self.race == "Elite":
            self.race = elite
        elif self.race == "Brute":
            self.race = brute
        elif self.race == "Grunt":
            self.race = grunt
        elif self.race == "Jackal":
            self.race = jackal
        elif self.race == "Hunter":
            self.race = hunter
        if self.current_loadout == "Air Assault":
            self.current_loadout = air_assault
    def cqc(self):
        if self.background == "cqc":
            self.race.strength += random.randint(0, 6)

    def engineer(self):
        if self.background == "engineer":
            self.race.tech += random.randint(0, 6)

    def sharpshooter(self):
        if self.background == "sharpshooter":
            self.race.precision += random.randint(0, 6)
    
    def demolitions(self):
        if self.background == "demolitions":
            pass
    
    def assault(self):
        if self.background == "assault":
            pass
    
    def recon(self):
        if self.background == "recon":
            pass
    
    def ODST(self):
        if self.background == "ODST":
            self.race.health += random.randint(0, 4)
            self.race.strength += random.randint(0, 4)
            self.race.speed += random.randint(0, 4)
            self.race.precision += random.randint(0, 4)
    
    def switch_weapon(self):
        if self.current_loadout.current_weapon == self.current_loadout.primary:
            self.current_loadout.current_weapon = self.current_loadout.secondary
        else:
            self.current_loadout.current_weapon == self.current_loadout.primary
    
    def show_character(self):
        print("Name: ", self.name)
        print("Race: ", self.race)
    
    def save_char(character):
        file = character.name + ".ddchar"
        with open(file, "w") as char_file:
            char_file.write(character.name + "\n")
            char_file.write(str(character.level) + "\n")
            char_file.write(character.race.name + "\n")
            char_file.write(character.current_loadout.name + "\n")

class Enemy(Character):

    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

def load_char(file):
    attr = []
    with open(file, 'r') as char_file:
        for line in char_file:
            line = line.strip()
            attr.append(line)
    char = Character(attr[0],attr[1],attr[2],attr[3].attr[4])
    return char


spartan = Race("Spartan", 15, 10, 10, 5, 20)
human = Race("Human", 10, 5, 5, 2)
elite = Race("Elite", 20, 12, 10, 4, 15)
brute = Race("Brute", 25, 20, 10, 2)
grunt = Race("Grunt", 10, 5, 2, 2)
jackal = Race("Jackal", 10, 5, 2, 8)
hunter = Race("Hunter", 30, 40, 7, 2)

cqc = "cqc"
engineer = "engineer"
sharpshooter= "sharpshooter"

chief = Character("John-117", 100, spartan, cqc, air_assault)
chief.save_char()