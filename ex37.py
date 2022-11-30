while True:
    try:
        num = float(input("Enter a number: "))
        break
    except:
        print("Enter a valid number.")
while num > 9:
        num = num + 2
        print(num)
print("Done")
  