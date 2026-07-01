#Q5. Write a program that keeps asking the user to enter numbers and stops when they type "stop", then prints how many numbers were entered (the count, not the sum).
x = input("Input your Number: ")
count = 0
while True:
    if x == "stop":
        break
    else:
        y = input("Input your Number: ")
        x = y
        count += 1

print(count)
