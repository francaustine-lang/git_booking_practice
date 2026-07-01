#Q9. Write a nested loop to print a multiplication table for numbers 6 to 10 (instead of 1–5).
count = 1
while count <= 5:
    for i in range(6, 11):
        print(i * count, " ")
        count += 1

    print
