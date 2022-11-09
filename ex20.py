# Import argv from sys module
from sys import argv 

# Assign command line arguments to variables
script, input_file = argv 

# Define a print all function which prints the content of content of the file 
def print_all(f):
    print(f.read())

# Rewinds our file to the original position
def rewind(f):
    f.seek(0)

# Print out a line number, followed by a line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open a file and assign it to a variable 
current_file = open(input_file)

print("First let's print the whole file:\n")

# Print out the content of the entire file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Rewind the file to the first position 
rewind(current_file)

print("Let's print three lines:")

# Set current line,print out each line of the file with the line number
current_line = 1 
print_a_line(current_line, current_file)

# increase the line number
# Set current line,print out each line of the file with the line number
current_line += 1
print_a_line(current_line, current_file)

#increase the line number
# Set current line,print out each line of the file with the line number
current_line += 1
print_a_line(current_line, current_file)