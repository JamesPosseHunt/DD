from weapons import *

class Loadout:

    def __init__(self, name, primary, secondary, aa, grenades):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.armor_ability = aa
        self.grenades = grenades
        self.current_weapon = primary

class ArmourAbility:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


jetpack = ArmourAbility("Jetpack", "Once every encounter, the character can use the jetpack to automatically evade one attack.")
sprint = ArmourAbility("Sprint", "Once every encounter, +2 to speed for the duration of that encounter.")
armour_lock = ArmourAbility("Armour Lock", "Once every encounter, the character can become immobile and impervious to damage for a turn. On their next turn, 2d8 damage is dealt to any enemies within a square of them.")
hologram = ArmourAbility("Hologram", "Once every encounter, the character can create a copy that runs across the field, drawing all enemy fire for a turn.")
drop = ArmourAbility("Drop Shield", "Once an encounter, the character can place a shield in front of them and their allies, with 10 hp.")
camo = ArmourAbility("Active Camouflage", "Once an encounter, for two turns, the character can become invisible and cannot be targeted by enemies.")
evade = ArmourAbility("Evade", "Once an encounter, the character can instantly jump 4 squares away from their target.")
charge = ArmourAbility("Hunter's Charge", "Once an encounter the Hunter can charge an enemy, doing 2d12 damage on contact.")

air_assault = Loadout("Air Assault", ar, magnum, jetpack, frag)
marksman = Loadout("Marksman", br, magnum, sprint, frag)
operator = Loadout("Operator", shotgun, magnum, armour_lock, frag)
grenadier = Loadout("Grenadier", grenade_launcher, magnum, hologram, frag)
ranger = Loadout("Ranger", storm, plasma_pistol, drop, plasma)
assassin = Loadout("Assassin", energy_sword, plasma_pistol, camo, plasma)
chieftain = Loadout("Chieftain", gravity_hammer, plasma_pistol, "Extra Shielding", plasma)
sniper = Loadout("Sniper", beam, plasma_pistol, evade, plasma)
hunter = Loadout("Hunter", assault_cannon, hunter_shield, charge, plasma)