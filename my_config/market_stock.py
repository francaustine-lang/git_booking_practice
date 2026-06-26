balance = int(input("Your Total Cash: "))
orange = 500
mangoe = 250
grape = 450
select = input("Select your item ('orange', 'mangoe', 'grape'): ")
if select == orange:
    select = orange
elif select == mangoe:
    select = mangoe
elif select == grape:
    select = grape

while True:
    if balance == 0:
        break
    else:
        balance = balance - select
print(balance)
