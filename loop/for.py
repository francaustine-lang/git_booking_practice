#determine whether it is a positive or negative number

x = int(input("Type any Number: "))
while True:
    if x > 0:
        message = "is Positive"
    else:
        message = "is Negative"
print(x, message)