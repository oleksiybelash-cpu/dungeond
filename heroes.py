import random

CLASSES = {
     "Warrior": {"hp": (110, 140), "attack": (10, 16)},
    "Archer": {"hp": (75, 90), "attack": (15, 20)},
    "Wizard": {"hp": (70, 90), "attack": (16, 24)},
    "Tank": {"hp": (150, 200), "attack": (5, 10)}
}


# def create_hero(name, hero_class):
#     stats = CLASSES[hero_class]
#     return {
#         "name": name,
#         "class": hero_class,
#         "hp": random.randint(*stats["hp"]),
#         "attack": random.randint(*stats["attack"]),
#     }
#
#
# def show_hero(hero):
#     print(f"  {hero['name']} — {hero['class']}")
#     print(f"  HP:     {hero['hp']}")
#     print(f"  Attack:  {hero['attack']}")

class Hero:
    game = "Dungeon code"
    count = 0
    def __init__(self, name, hero_class):
        Hero.count += 1
        stats = CLASSES[hero_class]
        self.name = name
        self.hero_class = hero_class
        self.max_hp = random.randint(*stats["hp"])
        self._hp = self.max_hp
        self.attack = random.randint(*stats["attack"])
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    def is_alive(self):
        return self._hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        return self.attack

    def __str__(self):
        return f"{self.name} ({self.hero_class}) HP {self.hp} / {self.max_hp} ATK {self.attack}"

    def __repr__(self):
        return f"Hero ({self.name!r}, {self.hero_class!r})"

