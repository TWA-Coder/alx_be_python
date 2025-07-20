number = int (input("Enter the size of the pattern: ")) 

t = 0

while t < number:
    for n in range(number):
        print("*", end="")
    t = t + 1

    print("\n")
