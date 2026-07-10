#Q4. Write a loop that prints all numbers from 1 to 30 that are divisible by 3.

emem = 3
while emem <= 30:
    print(emem)
    emem += 3

for number in range(1,31):
    if number % 3 == 0:
        print(number)

for number in range(3,31,3):
    print(number)
