from heroes import Warrior, Wizard
from enemies import Boss

CLASSES = {"1": Warrior, "2": Wizard}

choice = input("Choose your hero: 1 - Warrior, 2 - Mag: ")
name = input("Name of the hero: ")
hero = CLASSES.get(choice, Wizard)(name)

boss = Boss("King of Goblins", 120, 15)

round_no = 1

while hero.is_alive() and boss.is_alive():
    print(f"\n---- Round {round_no} ----")

    damage = hero.hit(enemy)
    print(f"{hero.name} hits {enemy.name}: -{damage} (hp of the enemy = {enemy.hp})")

    if enemy.is_alive():
        damage = enemy.hit(hero)
        print(f"{enemy.name} hits {hero.name}: -{damage} (hp of the hero = {hero.hp})")
    round_no += 1

if hero.is_alive():
    print("Victory!!!")
else:
    print("Game over!!!")