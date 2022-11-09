# # Define a function cheese_and_crackers with 2 parameters
# # Inside if the function use arguments with print statements
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")


# # Call our function with numbers as arguments
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)


# # Define 2 variables and assign them numbers
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# # Call our function with variables as arguments 
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# # Call our function and pass calculation as arguments
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# # Call our function and pass (calculation with variables) as arguments
# # print("And we can combine the two, variables and math:")
# # cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 

def add_two_numbers(number1, number2):
    print(f"{number1} + {number2} equals {number1 + number2}.")

add_two_numbers(1, 3)
add_two_numbers(2, 4)
add_two_numbers(2 + 3, 4 + 2)
add_two_numbers(7 - 3, 4 - 1)
add_two_numbers(3 + 5, 6 -2)


number1 = 2
number2 = 3

add_two_numbers(number1, number2)
add_two_numbers(number1 + 3, number2 -2)
add_two_numbers(number1 + number1, number2 + number2)
add_two_numbers(number1 - number2, number1 + number2)
add_two_numbers(number1 + number2 + number1, number2 + number1 + number2)