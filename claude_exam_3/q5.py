#Q5. Write a loop that keeps asking the user to guess a secret number (e.g. 7), 
#and tells them if their guess is too high, too low, or correct — stopping when they guess right.

number = 7
while True:
    guess = float(input("Guess a Number: "))
    if guess > number:
        print("Your GUESS is TOO HIGH")
    elif guess < number:
        print("Your GUESS is TOO LOW")
    else:
        print("Your GUESS is CORRECT")
        break
    