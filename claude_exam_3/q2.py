#Q2. Write a loop that prints every letter in a word entered by the user, one letter per line.

name = input("What is your name? ")
for i in name:
    print(i)

same = input("What is your name? ")
for index, i in enumerate(name, start = 1):
    print(f"{index}: {i}")