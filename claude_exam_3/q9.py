#Q9. Write a nested loop to print this pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end = ' ')
    print()

for i in range(6, 11):
    for j in range(6, i + 1):
        print(j, end = ' ')
    print()
