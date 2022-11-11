class Weapon:
    
    def __init__(self, name, damage, mag_size, mags, current_mag, type, base_crit, modes):
        self.name = name
        self.damage = damage
        self.mag_size = mag_size
        self.mags = mags
        self.current_mag = current_mag
        self.type = type
        self.base_crit = base_crit
        self.modes = modes

ar = Weapon(name="MA5B Assault Rifle", damage="2d8", mag_size=32, mags=12, current_mag=32, type="Kinetic", base_crit=1, modes=["Full Auto", "Burst"])
magnum = Weapon(name = "M6D Magnum Pistol", damage="2d8")
