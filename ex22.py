# setup 
mkdir
cd
ls

python3
quit()


# Exercise 1: a good program 

print()
python3 ex1.py

# Exercise 2: Comments and pound characters

# comment  


# Exercise 3: Numbers and Math 

# Math symbols / operators: 
+ -, %, *, <, >, =, +=, 
print("Hens", 25 + 34 / 5)

# Exercise 4: Variables and Names 
cars = 100


# Exercise 5: More variables and printing

my_name = 'Myers O. Butera'
print("Let's talk about {my_name}.") # format string 

# Exercise 6: Strings and text 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} "

print(joke_evaluation.format{hilarious})

# Exercise 7: More printing
ending1 ="C"
ending2 = "h"
ending3 = "e"

printing(end1 + end2 + end3, end='')

# Exercise 8 : Printing, printing

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format(True, False, False, True))

# Exercise 9: Printing, printing, printing

print("""
 There's something going on here.
 With the three double-quotes.
 We'll be able to type as much as we like.
 Even 4 lines if we want, or 5, or 6
""")

# Exercise 10: What was that? 

tabby_cat = "\t I'm tabbed in."  # Escape sequences 
backslash_cat = "I'm \\ a \\ cat."

# Exercise 11: Asking questions 
print("How old are you?", end='')
age = input()  # input() function collect user input 

# Exercise 12: Prompting people

age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(f"So,you're {age}old, {height} tall and {weight}  heavy.")

# Exercise 13: Parameters, Unpacking, Variables 

from sys import argv 
Script, first, second, third = argv 

# Exercise 14: Prompting and passing 

prompt = '> '
likes = input(prompt)

# Exercise 15: Reading Files 

txt = open(filename)
print(txt.read())

# Exercise 16: Reading and writing files 

target = open(filename, 'w')
target.truncate()    # truncate empties the file 
target.write(line1)
target.close()

# seek(0) --Move the read/write location to the beginning of the file 

# Exercise 17: More Files 

from os.path import exists 
Print(f"Does the output file exists?{exists(to_file)}")

# Exercise 18: Names, Variables, Code, Functions 

def print_two(*args):
    arg1, arg2 = args 
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Myers", "Butera")
print_two_again("Myers", "Butera")

# Exercise 19: Functions and Variables 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Exercise 20: Functions and Files 

def print_a_line(line_count, f):
    print(line_count, f.readline())  # readline -> reads a file one line at a time 

current_line += 1

# Exercise 21: Functions can return something 

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

age = add(30, 5)