#Q2. Write a loop that calculates the factorial of a number 
# (e.g., factorial of 5 = 5×4×3×2×1 = 120).

numb = int(input("YOUR NUMBER: "))
result = 1
for i in range(1, numb + 1):
    result = result * i
print(result)
