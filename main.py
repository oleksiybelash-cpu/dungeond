from heroes import Hero
from enemies import Enemy

hero = Hero("Nova", "Wizard")
enemy = Enemy("Goblin", 60, 9)

round_no = 1

while hero.is_alive() and enemy.is_alive():
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