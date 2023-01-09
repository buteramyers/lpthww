import sys 
import os 
import random
import time 


def print_slow(str, delay = 0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")


def reset_console():
    print("\n")
    os.system('cls||clear')


def fprint(str, delay = 0):
    print("\n" + str)
    time.sleep(delay)


def sprint(str, delay = 0):
    print(str)
    time.sleep(delay)


player = {"location":"", "health":100, "items":[]}


class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        fprint(f"A {self.name} emerges from the shadows.")
        fprint("Hissss! Stay away from me!")

    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)


goblin = NPC("goblin", "hallway")


def entry():
    player["location"] = "entry"  
    print(f"\nHealth:{player['health']}")
    fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
    print("Ahead, you can see a cavern. Will you continue?")
    medkit_find = random.choice([True,False])
    if medkit_find == True:
        medkit = True
        fprint("You found a mdekit!")
        print("Enter 'm' to use it.")
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            cavern()
        elif action == "no":
            fprint("A bat flies over your head and you screetches in the distance.")
        elif action == "m":
            use_medkit()
        else:
            fprint("You sit in total darkness wondering if there's a way out.")


def cavern():
    player["location"] = "cavern" 
    print(f"\nHealth:{player['health']}")
    fprint("You stumble into a dimly lit cavern.", 2)
    print("You cannot go right or left but the cave continues ahead. Will you go on?")
    bat_attack = random.choice([True,False])
    bat_attack = True
    if bat_attack == True:
        fprint("You were attacked by a bat!")
        health -= random.randint(1,100)
        print(f"\nHealth:{health}")
        if health == 0:
            fprint("You are dead!")
            sys.exit()
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            hallway()
        elif action == "no":
            fprint("You sit down and eat some food you brought with you.")
        elif action == "m":
            use_medkit()
        else:
            fprint("You shiver from the cold.")


def hallway():
    player["location"] = "hallway" 
    print(f"\nHealth:{player['health']}")
    fprint("You are in a wide hallway. It continues on indefinitely", 2)
    print("There's no turning back. Will you go on?")
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            pit()
        elif action == "no":
            fprint("You try to call for help but no one is there.")
        elif action == "m":
            use_medkit()
        else:
            fprint("You wonder what time it is.")


def pit():
    player["location"] = "pit" 
    print(f"\nHealth:{player['health']}")
    fprint("You fall head first into an ominous and languid pit.", 2)
    sprint("Luckily you only landed on your back.",2)
    print("You can climb out. Will you try?")
    handle_goblin()
    while True:
        action = input("\n> ")
        if action == "yes":
            fprint("You try to climb out but you slide off the rocky walls and fall down again.",2)
            print("GAMEOVER!")
            sys.exit()
        elif action == "no":
            fprint("You sit in utter darkness.")
        elif action == "m":
            use_medkit()
        else:
            fprint("You feel hopeless.")


def use_medkit():
    if "medkit" in player["items"]:
        player['items'].remove("medkit")
        fprint("You used your medkit")
        player['health'] = 100
        print(f"\nHealth:{player['health']}")
    else:
        fprint("You don't have a medkit.")


def handle_goblin():
    goblin.move()
    if player["location"] == goblin.location:
        goblin.talk()


entry()