import random
#hero = {
#   "name": "John",
#   "class": "Warrior",
#   "Hp": 80,
#    "Damage": 15,
#}

#print("name: ", hero["name"])
#print("class: ", hero["class"])
#print("Hp: ", hero["Hp"])
#print("Damage: ", hero["Damage"])

Classes = {
    "Warrior": {"Hp": (100, 140), "Damage": (10, 15)},
    "Wizard": {"Hp": (75, 90), "Damage": (20, 30)},
    "Archer": {"Hp": (75, 90), "Damage": (15, 20)},
    "Tank": {"Hp": (150, 200), "Damage": (5, 10)}
}

def create_hero(name, hero_class):
    stats = Classes[hero_class]
    return {
        "name": name,
        "class": hero_class,
        "Hp": random.randint(*stats["Hp"]),
        "Damage": random.randint(*stats["Damage"]),
    }

def show_hero(hero):
    print(f"{hero['name']} - {hero['class']}")
    print(f"HP: {hero['Hp']}")
    print(f"Damage: {hero['Damage']}")
John = create_hero("John", "Warrior")
Jake = create_hero("Jake", "Wizard")
Anna = create_hero("Anna", "Archer")
Ben = create_hero("Ben", "Tank")
show_hero(John)
show_hero(Jake)
show_hero(Anna)
show_hero(Ben)
