#Q1. Write a loop to print all even numbers between 1 and 20 (inclusive).
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end = '\t')
print()

even = 2
while even <= 20:
    if even % 2 == 0:
        print(even, end = '\t')
    even += 1
print()

for eve in range(2, 21, 2):
    print(eve, end = '\t')