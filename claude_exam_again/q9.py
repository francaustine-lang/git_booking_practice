#Q9. A word = "programming", use a loop to count how many vowels are in it (without using any built-in vowel-counting function).
word = 'programming'
vowel = 'aeoui'

count = 0
for char in word:
    if char in vowel:
        count += 1
    
print(count)