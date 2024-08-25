class Enemy:
    type_of_enemy:str
    health_points:int=10
    attack_damage:int =1
    def talk(self):
        print("I am an Enemy")
    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')
    def attack(self):
        print(f"f{self.type_of_enemy} attacks for {self.attack_damage} damage")
    ##Default constructor that automatically python create it
    def __init__(self):
        print("new Enemy created with no starting values \n")
    def _init_(self,type_of_enemy,health_points=10,attack_damage=1):
        self.type_of_enemy=type_of_enemy
        self.health_points=health_points
        self.attack_damage=attack_damage
