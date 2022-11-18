print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    print("You find yourself in the future; 2050 to be exact")
    print("What is the first thing you're gonna do ?")
    print("1. Get a job like a normal person and get paid.")
    print("2.Get a newspaper to what changed over the years.")

    future = input("> ")

    if future == "1":
        print("You find out that the system is being run by black niggas and white folks are actually getting buried in debt from over working and little pay.")
    elif future == "2":
        print("You find out that the scientists actually made contact with an alien species and that didn't end well")
        print("to the point of nearly wiping out our civilization due to a conflict with the alien community abpuction of some people for research purposes.")
    else:
        print("Lose your mind and run crazy on the streets telling everybody that you're a time-traveller")
        print("Then you get kidnapped by government officials for investigation on how you did it and some harsh experiments")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1.Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("Good pick! Now pick a price")
    print("1.Dollars")
    print("2.Object of surprise")

    price = input("> ")

    if price == "1":
      print("Lucky pick! So you get 5000 dollars.Good job!")
    elif price == "2":
        print("You prolly thought it was some nice ryt.But guess what?You get a pair of socks instead!")
        print("Hahahaha make better choices next time ok!")
    else: 
        print("Are you telling me that you can't make a damn decision?")
        print("The hell out ma face!") 


else:
    print("Get your scared ass outta here what kind of paranoia makes u afraid of picking a door.")