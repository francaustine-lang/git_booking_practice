#Q5. Given numbers = [4, 8, 15, 16, 23, 42], 
# use a loop to find and print the largest number without using max().

numbers = [4, 8, 15, 16, 23, 42],
result = []
for i in numbers:
    if i >= result:
        i = result
    print(i)    