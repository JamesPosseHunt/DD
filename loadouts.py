from weapons import *

class Loadout:
    
    def __init__(self, name, primary, secondary, aa, grenades):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.armor_ability = aa
        self.grenades = grenades
