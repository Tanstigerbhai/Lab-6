# prompting the user ti enter the number and limit
number = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up to which you want thebmultiplcation table generated: "))

# generating the multoplication table
print(f"multiplication table for {number}:")
for i in range(1, limit + 1):
    result = number * i
    print(f"{number} * {i} = {result}")
