from sys import exit 

def break_time():
    print("You go out and find your friends having their break besides the playground")
    assignment_done = False 

    while True:
        choice = input("> ")

        if choice == "ask them about the assignment" and not assignment_done:
            print("Some tell you they brought it and others are in the same situation as you.")
            print("So they give you their work and you write it down")
            print("The break gets over and now it's time to go to class.")
            assignment_done = True
        elif choice == "ask them about the assignment"and assignment_done:
            dead("You find that none of them even have their books with them at the moment.")
        elif choice == "you don't ask about the assignment":
            dead("You go and tell stories with you're friends til the break is over.")
        elif choice == "go to class" and assignment_done:
            another_class_room()
        else:
            dead("Say something that makes sense.")

def another_class_room():
    print("You get in class ready for the next lesson")
    print("As the teacher is talking, he remembers about the due assignments.") 
    print("Then he starts asking people to hand-in the work.")

    choice = input("> ")

    if choice == "you hand-in the work":
        print("The teacher congratulates you for doing work on time!")
        dead("You did it! Up next is the other version of the game which is coming real soon.")
    elif choice == "you dont'":
        dead("Everyone gives out their work except you and you lose marks on ur report.")
    else:
        dead("do something!") 

# execute the class_room code, ask for user choice 
def class_room():
    print("You enter class scared shitless.")
    print("You're too scared to even look at the teacher in class.")
    print("Then you find out that the teacher actually forgot about the assignment.")
    print("Are you gonna remind him or jus wait for everything to playout smoothly?")
    teacher_reminded = False 

    while True:
        choice = input("> ")

        if choice == "ask him":
            dead("The teacher remembers and asks everyone for the work including you.")
        elif choice == "say nothing" and not teacher_reminded:
            print("The class goes on as usual and you finally reach break time!")
            print("Break time reaches so you're free to go out of class for a break.")
            teacher_reminded = True
        elif choice == "say nothing" and teacher_reminded:
            dead("The teacher eventually remembers in the course of the class and punishes the whole class.")
        elif choice == "go out" and teacher_reminded:
            break_time()
        else:
            print("I got no idea what that means.")

# execute Cthulhu_room code, ask for user choice
def home():
    print("Here is where you start to look for a valid reason that allows you to stay home.")
    print("You stay in bed and continue brainstorming for ideas.")
    print("Your mom enters the room and tells you that if you stay in bed you'll run late.")
    bed_room = False

    while True:
        choice = input("> ")

        if choice == "stall her":
            print("You buy yourself time.")
            dead("But you endup going to school late either way.")
        elif choice == "lie to her" and not bed_room:
            print("She gets you and let's you stay home.")
            bed_room = False 
        elif choice == "lie to her" and bed_room:
            print("She catches you lying to her and punishes you.")
            dead("Takes you to school and talks to your teacher aswell.")
        elif choice == "stay in bed" and bed_room:
            bed_room()  
        elif "tell her the truth" in choice :
            print("She doesn't buy your fake reason and gets pissed!")
            dead("You get bitten up and still get to go to school either way!")
        else:
            dead("Quit delaying and say something!")


def bed_room():
    print("So you stay in your room and and take a shower later.")
    print("She leaves for work along with with your dad.")


def dead(why):
    print(why, "Good job!")
    exit(0)

# print out instructions and get the user's choice
def start():
    print("You have jus woken up.")
    print("And you realise there alot of undone work that you got.")
    print("But you remember that it's a school day and you gotta go.")
    print("What are you gonna do ?")

    choice = input("> ")

    if choice == "go to school":
        class_room()
    elif choice == "stay home":
        home()
    else:
        dead("You end up getting late and get your butt kicked at school.")


# execute start function
start()