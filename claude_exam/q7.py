#Q7. Write a loop that prints this pattern:
#5
#4 4
#3 3 3
#2 2 2 2
#1 1 1 1 1

number = 5
position = 1
while number >=1:
    message = str(number) + " "
    print(message * position)
    number -= 1
    position += 1 