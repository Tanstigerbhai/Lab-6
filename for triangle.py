# prompting  the user to enter the height of the triangle
height = int(input("Enter the height of the triangle (number of rows): "))

# generating the pattern of the stars
print("pattern of stars:")
for i in range(1, height + 1):
    print("*" * i)
