#Q5. Given numbers = [4, 8, 15, 16, 23, 42], 
# use a loop to find and print the largest number without using max().

number = [4, 8, 15, 16, 23, 42]
big = [0]

for i in number:
    
    if i > big:
        big.append(i)
        print(big)
        print()