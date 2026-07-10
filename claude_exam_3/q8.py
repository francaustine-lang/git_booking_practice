# Q8. Write a loop to print the first 10 Fibonacci numbers: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


a, b = 0, 1
count = 0
while count < 10:
    print(a, end = '\t')
    a, b = b, a + b
    count += 1

