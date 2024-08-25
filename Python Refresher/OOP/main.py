from Dog import *
from Enemy import *
"""
zombie=Enemy()
zombie.type_of_enemy="zomibeeeee"
print(f"{zombie.type_of_enemy} has {zombie.health_points} health points "
      f"and can do attack of {zombie.attack_damage}")

zombie.talk()
zombie.walk_forward()
zombie.attack()
"""
zombie=Enemy("zombie",15,3)

print(f"{zombie.type_of_enemy} has {zombie.health_points} health points "
      f"and can do attack of {zombie.attack_damage}")
