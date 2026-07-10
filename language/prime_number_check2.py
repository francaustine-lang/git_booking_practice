x = int(input("Input any Number: "))
is_prime = True
for i in range(2, x):
    if x % i == 0:
        print(x, "divided by", i, " gives a zero remainder")
        is_prime = False
        break


