# a loop that performs continuos addition

initial = 0
while True:
    
    follow_up = int(input("INPUT ANY NUMBER: "))
    if follow_up == 0:
        break
    initial = initial + follow_up

print("The sum of your Numbers is: ", initial)