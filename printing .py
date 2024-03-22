# printing numbers from 1 to 9, skipping 3 in the inner loop, and braking out at 7
print("numbers from 1 to 9, skipping 3 in the inner loop, and breaking out at 7:")
for i in range (1,10):
    if i == 3:
        break
    for j in range (1,4):
        if i == 3:
            continue
        print(i,end =" ")
    print()    