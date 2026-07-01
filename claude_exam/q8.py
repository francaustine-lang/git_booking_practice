#Q8. Write a program that uses a loop to print all prime numbers between 1 and 50.
num = 2
while num <= 50:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        
    num += 1
