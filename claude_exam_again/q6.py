#Q6. Write a loop that prints numbers from 1 to 50, 
# but skips any number divisible by 3 or 5 (use continue).
arc = 0
bet = 1
for numb in range(1, 51):
    if numb % 3 == 0 or numb % 5 == 0:
        arc.append(numb)
    else:
        bet.append(numb)
print(arc)
    
