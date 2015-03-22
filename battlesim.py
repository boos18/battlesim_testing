import random

weapons = {0: 'SA_Rifle', 1: 'A_Rifle', 2: 'Pistol', 3: 'Shotgun', 4: 'Knife'}
weapon_ranges = {'SA_Rifle': 8, 'A_Rifle': 6, 'Pistol': 5, 'Shotgun': 4, 'Knife': 1}
weapon_damage = {'SA_Rifle': 5, 'A_Rifle': 8, 'Pistol': 3, 'Shotgun': 5, 'Knife': 3}
armors = {0: 'no_armor', 1: 'kevlar_vest'}
armor_points = {'no_armor': 0, 'kevlar_vest': 4}

class Soldier():
    dead = False
    def __init__(self, name, hp, sol_weapon, sol_armor, dexterity, strength):
        self.name = name
        self.hp = hp
        self.sol_weapon = weapons[sol_weapon]
        self.sol_armor= armors[sol_armor]
        self.dexterity = dexterity + 2
        self.strength = strength + 2


    def calculate_offensive_damage(self, current_range, target):
        if self.dead == False:
            dmg = 0
            print("Soldier {0} has a {1}".format(self.name, self.sol_weapon))
            #print(weapon_ranges[self.sol_weapon])
            if weapon_ranges[self.sol_weapon] >= current_range:
                shot = random.randrange(10)
                print("{0} Shoots at {1}! He rolls {2}, his target roll is below {3}. And...".format(self.name, target.name, shot, self.dexterity))
                if shot <= self.dexterity:
                    dmg = random.randrange(weapon_damage[self.sol_weapon]) + 1
                    dmg = dmg - armor_points[target.sol_armor]
                    print("Hits! For {0}".format(dmg))
                else:
                    print("Misses!")
            else:
                print("{0} is Out of range!".format(target.name))
            return dmg
        else:
            print("{0} is dead and can't fire.".format(self.name))
            return 0
    def calculate_taken_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.dead = True

    def print_soldier(self):
        print("Soldier {0} has {1} hp, a {2}, {3} dex, {4} str. He's armor is {5}.".format(self.name, self.hp, self.sol_weapon, self.dexterity, self.strength, self.sol_armor))


sol1 = Soldier("Bruce Willis", random.randrange(10), random.randrange(4), random.randrange(1), random.randrange(10), random.randrange(10))
sol2 = Soldier("Kirk Douglas", random.randrange(10), random.randrange(4), random.randrange(1), random.randrange(10), random.randrange(10))

redteam = [sol1]
blueteam = [sol2]


for s in redteam:
    s.print_soldier()
for s in blueteam:
    s.print_soldier()

sol2.calculate_taken_damage(sol1.calculate_offensive_damage(7, sol2))