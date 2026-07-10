#Q4. Given this list: numbers = [3, 6, 9, 2, 7, 4, 8, 1, 5]
#Use a loop to separate and print the even and odd numbers into two separate lists.

numbers = [3, 6, 9, 2, 7, 4, 8, 1, 5]
print("The Odd Numbers include:")
for i in numbers:
    if i % 2 == 1:
        print(i, end="\t")
print("\nThe Even Numbers include: ")
for j in numbers:
    if j % 2 == 0:
        print(j, end = "\t")

numb = [3, 6, 9, 2, 7, 4, 8, 1, 5]
even = []
odd = []
for i in numb:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("\n\nEven: ", even)
print("Odd: ", odd) 