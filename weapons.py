class Weapon:
    
    def __init__(self, name, damage, base_crit, ammo_type):
        self.name = name
        self.damage = damage
        self.ammo_type = ammo_type
        self.base_crit = base_crit
    

class Gun(Weapon):

    def __init__(self, name, damage, mag_size, mags, current_mag, type, base_crit, modes):
        self.name = name
        self.damage = damage
        self.mag_size = mag_size
        self.mags = mags
        self.current_mag = current_mag
        self.type = type
        self.base_crit = base_crit
        self.modes = modes

class Grenade(Weapon):

    def __init__(self, name, damage, base_crit, count):
        self.name = name
        self.damage = damage
        self.base_crit = base_crit
        self.count = count

class Melee(Weapon):
    
    def __init__(self, name, damage, base_crit, charge, range):
        self.name = name
        self.damage = damage
        self.charge = charge
        self.range = range
        self.base_crit = base_crit

ar = Gun("MA5D Assault Rifle", "2d8", 32, 8, 32, "Kinetic", 1, ["Full Auto", "Burst"])
magnum = Gun("M6H Magnum Pistol", "2d8", 12, 5, 12, "Kinetic", 2, ["Single-shot"])
br = Gun("BR85 Battle Rifle", "2d8", 36, 4, 36, "Kinetic", 2, ["Burst"])
shotgun = Gun("M45D Tactical Shotgun", "2d12", 6, 4, 6, "Kinetic", 1, ["Single-shot"])
grenade_launcher = Gun("M319 Grenade Launcher", "2d12", 1, 16, 1, "Power", 1, ["SIngle-shot"])
storm = Gun("Storm Rifle", "2d8", 200, 1, 200, "Plasma", 1, ["Full Auto"])
plasma_pistol = Gun("Plasma Pistol", "2d8", 100, 1, 100, "Plasma", 2, ["Single-shot", "Overcharge"])
spiker = Gun("Spiker", "2d8", 40, 4, 40, "Kinetic", 2, ["Burst"])
beam = Gun("Beam Rifle", "2d12", 10, 1, 10, "Plasma", 2, ["Single-shot"])
assault_cannon = Gun("Assault Cannon", "2d12", 20, 5, 20, "Fuel Rod", 3, ["Single-shot"])
suppressor = Gun("Suppressor", "2d8", 36, 7, 36, "Hardlight", 2, ["Full Auto"])
boltshot = Gun("Boltshot", "2d8", 10, 4, 10, "Hardlight", 2, ["Single-shot", "Overcharge"])
lightrifle = Gun("Lightrifle", "2d8", 36, 4, 36, "Hardlight", 3, ["Single-shot", "Scoped"])
scattershot = Gun("Scattershot", "2d8", 5, 4, 5, "Hardlight", 2, ["SIngle-shot"])

energy_sword = Melee("Energy Sword", "2d20", 5, 100, 2)
gravity_hammer = Melee("Gravity Hammer", "2d20", 5, 100, 3)
hunter_shield = Melee("Hunter's Shield", "40", 2, 0, 1)
melee = Melee("Melee", "2d4", 2, 0, 1)
knife = Melee("Combat Knife", "2d6", 5, 1, 1)


frag = Grenade("M9 Frag Grenade", "2d20", 4, 2)
plasma = Grenade("Plasma Grenade", "2d20", 4, 2)