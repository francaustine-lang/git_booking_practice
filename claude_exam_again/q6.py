#Q6. Write a loop that prints numbers from 1 to 50, 
# but skips any number divisible by 3 or 5 (use continue).
for numb in range(1, 51):
    if numb % 3 == 0 or numb % 5 == 0:
        continue
    print(numb, end='\t')
    
