#Q6. Write a loop that prints the FizzBuzz pattern from 1 to 30:
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:       #Print FizzBuzz if divisible by both
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:     #Print Fizz if divisible by 3
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:     #Print Buzz if divisible by 5
        print("Buzz")
    else:
        print(i)                        #Otherwise print the number

for j in range(1, 31):
    if j % 3 == 0 and j % 5 == 0:       #Print FizzBuzz if divisible by both
        print("FizzBuzz")
    elif j % 3 == 0:                    #Print Fizz if divisible by 3
        print("Fizz")
    elif j % 5 == 0:                    #Print Buzz if divisible by 5
        print("Buzz")
    else:
        print(j)                        #Otherwise print the number