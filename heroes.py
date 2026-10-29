import random
from characters import Character
from main import damage


class Hero(Character):
    title = "Hero"
    def __init__(self, name, max_hp, attack):
        super().__init__(name, max_hp, attack)
    def special(self, target):
        return self.hit(target)
    def __str__(self):
        return f"{self.name} {super().__str__()}"
class Warrior(Hero):
    title = "Warrior"
    def __init__(self, name):
        super().__init__(name, random.randint(100,125), random.randint(10, 15))

    def special(self, target):
        damage = int(self.attack * 1.5)
        target.take_damage(damage)
        return damage

class Wizard(Hero):
    title = "Wizard"

    def __init__(self, name):
        super().__init__(name, random.randint(70, 90), random.randint(20, 25))
        self.mana = 30

    def special(self, target):
        if self.mana < 10:
            print(f"{self.name}: too little mana, basic hit.")
            return self.hit(target)

        self.mana -= 10
        damage = self.attack * 2
        target.take_damage(damage)
        return damage