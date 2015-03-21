import random

weapons = {0: 'SA_Rifle', 1: 'A_Rifle', 2: 'Pistol', 3: 'Shotgun', 4: 'Knife'}
weapon_ranges = {'SA_Rifle': 8, 'A_Rifle': 6, 'Pistol': 5, 'Shotgun': 4, 'Knife': 1}
weapon_damage = {'SA_Rifle': 5, 'A_Rifle': 8, 'Pistol': 3, 'Shotgun': 5, 'Knife': 3}


class Soldier():

    def __init__(self, name, hp, sol_weapon, dexterity, strength):
        self.name = name
        self.hp = hp
        self.sol_weapon = weapons[sol_weapon]
        self.dexterity = dexterity
        self.strength = strength

    def calculate_damage(self, current_range):

        dmg = 0
        print("Soldier {0} has a {1}".format(self.name, self.sol_weapon))
        print(weapon_ranges[self.sol_weapon])
        if weapon_ranges[self.sol_weapon] >= current_range:
            shot = random.randrange(10)
            print("{0} Shoots! He rolls {1}. And...".format(self.name, shot))
            if shot <= self.dexterity:
                dmg = weapon_damage[self.sol_weapon]
                print("Hits! For {0}".format(dmg))
            else:
                print("Misses!")
        return dmg



sol1 = Soldier("Bruce Willis", random.randrange(10), random.randrange(4), random.randrange(10), random.randrange(10))

print("Soldier {0} has {1} hp, a {2}, {3} dex, {4} str".format(sol1.name, sol1.hp, sol1.sol_weapon, sol1.dexterity, sol1.strength))


sol1.calculate_damage(5)