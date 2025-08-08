class Player:
    def __init__(self, name, position=(0, 0)):
        self.name = name
        self.position = position
        self.health = 100

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

class Enemy:
    def __init__(self, enemy_type, position=(0, 0)):
        self.enemy_type = enemy_type
        self.position = position
        self.health = 50

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def attack(self, player):
        player.take_damage(10)  # Example damage value

    def is_alive(self):
        return self.health > 0