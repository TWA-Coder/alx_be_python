number = int(input("Enter a number to see its multiplication table: "))

list = [1,2,3,4,5,6,7,8,9,10]

for n in list:
    print(f"{number} * {n} =", number * n)