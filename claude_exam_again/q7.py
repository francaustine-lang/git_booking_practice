#Q7. Use a loop to check whether a given number is prime. 
# Test it with n = 29.

a = int(input("INPUT YOU NUMBER: "))
for i in range(1, a):
    is_prime = True
    if a % i == 0:
        is_prime = False

if True:
    print(a, "IS PRIME")


print()