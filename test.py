from rpg0 import Hero
from rpg0 import Goblin

# give hero and goblin health and power
hero = Hero(10, 5)
goblin = Goblin(6, 2)

# check health and power of hero and goblin
# fight / do nothing/ flee depend on user input
hero.attack(goblin)

