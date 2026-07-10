a = int(input("Input any Number: "))

if a <= 1:
    print(a, " is a Prime Number")
else:
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break

if is_prime:
    print(a, " is a Prime Number")
    
else:
    print(a, "is not a Prime Number")
    


