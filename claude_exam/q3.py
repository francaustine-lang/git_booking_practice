#Q3. Given this list: animals = ["cat", "dog", "rabbit", "horse"]
#Write a loop that prints each animal along with its position (e.g., "1: cat", "2: dog"...)

animals = ["cat", "dog", "rabbit", "horse"]
for index, animal in enumerate(animals, start=1):
    print( index,":", animal)

rabbi = ["cat", "dog", "rabbit", "horse"]
for index, animal in enumerate(rabbi, start=1):
    print(f"{index}: {animal}")

bill = ["cat", "dog", "rabbit", "horse"]
skill = 1
for animal in bill:
    print(f"{skill}: {animal}")
    skill += 1