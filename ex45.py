import sys 
import os 
import random
import time 


class Game:

    def print_slow(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")


    def reset_console(self):
        print("\n")
        os.system('cls||clear')


    def fprint(self, str, delay = 0):
        print("\n" + str)
        time.sleep(delay)


    def sprint(self, str, delay = 0):
        print(str)
        time.sleep(delay)

game_functions = Game()

class Player:
    def __init__(self, location, health, items):
        self.health = health
        self.items = items


hero = Player("entry", 100, []) 

class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.fprint(f"A {self.name} emerges from the shadows.")
        game_functions.fprint("Hissss! Stay away from me!")

    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)


goblin = NPC("goblin", "hallway")

class World:
    
    def entry(self):
        hero.location = "entry"  
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
        print("Ahead, you can see a cavern. Will you continue?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.cavern()
            elif action == "no":
                game_functions.fprint("A bat flies over your head and you screetches in the distance.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You sit in total darkness wondering if there's a way out.")


    def cavern(self):
        hero.location = "cavern" 
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You stumble into a dimly lit cavern.", 2)
        print("You cannot go right or left but the cave continues ahead. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.check_bat_attack()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.hallway()
            elif action == "no":
                game_functions.fprint("You sit down and eat some food you brought with you.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You shiver from the cold.")


    def hallway(self):
        hero.location = "hallway" 
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You are in a wide hallway. It continues on indefinitely", 2)
        print("There's no turning back. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.pit()
            elif action == "no":
               game_functions.fprint("You try to call for help but no one is there.")
            elif action == "m":
                self.use_medkit()
            else:
               game_functions.fprint("You wonder what time it is.")


    def pit(self):
        hero.location = "pit" 
        print(f"\nHealth:{hero.health}")
        game_functions.fprint("You fall head first into an ominous and languid pit.", 2)
        game_functions.sprint("Luckily you only landed on your back.",2)
        print("You can climb out. Will you try?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                game_functions.fprint("You try to climb out but you slide off the rocky walls and fall down again.",2)
                print("GAMEOVER!")
                sys.exit()
            elif action == "no":
                game_functions.fprint("You sit in utter darkness.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You feel hopeless.")


    def use_medkit(self):
        if "medkit" in hero.items:
            hero.items.remove("medkit")
            game_functions.fprint("You used your medkit")
            hero.health = 100
            print(f"\nHealth:{hero.health}")
        else:
            game_functions.fprint("You don't have a medkit.")


    def handle_goblin(self):
        goblin.move()
        if hero.location == goblin.location:
            goblin.talk()


    def check_medkit(self):
        medkit_find = random.choice([True,False])
        if medkit_find == True:
            medkit = True
            game_functions.fprint("You found a medkit!")
            print("Enter 'm' to use it.")


    def check_bat_attack(self):
        bat_attack = random.choice([True,False])
        if bat_attack == True:
            game_functions.fprint("You were attacked by a bat!")
            hero.health -= random.randint(1,100)
            print(f"\nHealth:{hero.health}")
            if hero.health == 0:
                game_functions.fprint("You are dead!")
                sys.exit()

new_world = World()


new_world.entry()