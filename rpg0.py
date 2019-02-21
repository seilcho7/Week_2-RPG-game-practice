"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
# Character class
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True

# Hero class inherit from Character class
class Hero(Character):
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
    
    def attack(self, goblin):
        while goblin.alive() and self.alive():
            self.print_status()
            goblin.print_status()
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = input()
            if user_input == "1":
                # Hero attacks goblin
                goblin.health -= self.power
                print("You do %d damage to the goblin." % self.power)
                if goblin.health <= 0:
                    print("The goblin is dead.")
            elif user_input == "2":
                goblin.attack(self)
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)

# Goblin class inherit from Character class
class Goblin(Character):
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

    def attack(self, hero):
        if self.health > 0:
            # Goblin attacks hero
            hero.health -= self.power
            print("The goblin does %d damage to you." % self.power)
            if hero.health <= 0:
                print("You are dead.")

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have %d health and %d power." % (hero_health, hero_power))
#         print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ",)
#         user_input = input()
#         if user_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do %d damage to the goblin." % hero_power)
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input %r" % user_input)

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does %d damage to you." % goblin_power)
#             if hero_health <= 0:
#                 print("You are dead.")

# main()