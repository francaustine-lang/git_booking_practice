#Q3. Write a program that uses a loop to calculate the factorial of a number entered by the user.
#(e.g. factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120)
x = 1
y = int(input("Input a number: "))
for i in range(1, y+1):
    x = i * x
print(x)

