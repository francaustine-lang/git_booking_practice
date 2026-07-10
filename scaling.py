#Q3. Use a while loop to print the Fibonacci sequence up to the 10th term 
# (0, 1, 1, 2, 3, 5, 8...).
x, y = 0, 1
#y = 1
count = 0
while count < 10:
    print(x, end = "\t")
    x, y = y, x + y
    #y = x + y
    count += 1