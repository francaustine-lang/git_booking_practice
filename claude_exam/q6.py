#Q6. Given this list: scores = [55, 89, 42, 67, 91, 38, 74]
#Use a loop to find and print the smallest number (without using min()).
scores = [55, 89, 42, 67, 91, 38, 74]
least = scores[0]
for i in scores:
    if least > i:
        least = i

print(least)