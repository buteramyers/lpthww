numbers = []

def iterate(iteration, inc):
    # i = 0
    for i in range(0, iteration, inc):
        print(f"At the top i is {i}")
        numbers.append(i)

        # i += inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

iterate(10, 2) 

print("The numbers: ")

for num in numbers:
    print(num)