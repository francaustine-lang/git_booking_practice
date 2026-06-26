number = 0
while True:
    b = int(input("Any Number: "))
    if b == 0:
        break
    number = b - number
print("Subtraction of your numbers: ", number)