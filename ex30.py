# Define a variable with an integer value
people = 40 
cars = 30 
trucks = 55

# Checking if cars are greater than people or them being greater than cars
if cars > people and trucks > cars:
    print("We should take the cars.")
    #Otherwise check if cars are less than people
elif cars < people:
    print("We should not take the cars.")
    # if neither if and elif is tru then run the else statement
elif trucks > people:
    print("There is too many trucks")
else:
    print("We can't decide.")
# check if trucks is greater than people and people is smaller than trucks 
if trucks > cars and people < trucks:
    print("That's too many trucks.")
    # otherwise check if trucks is smaller than cars 
elif trucks < cars: 
    print("Maybe we could take the trucks.")
    #if niether if or elif condition is true, print the else statement
else: 
    print("We still can't decide.")

#check if people isnot larger than trucks
if not(people > trucks): 
    print("Alright, let's just take the trucks.")
# otherwise  if is false , print out else statement
else:
    print("Fine, let's stay home then.")