#Q10. Use a loop to count how many vowels (a, e, i, o, u) are in a given string, e.g. "Francaustine".
name = "Francaustine"
vowel = "aeiou"
count = 0
for i in name:
    for j in vowel:
        if i == j:
            count +=1
print(count)

#Q10. Use a loop to count how many vowels (a, e, i, o, u) are in a given string, e.g. "Francaustine".
name = "Thunder waec"
vowel = "aeiou"
count = 0
for i in name:
    if i in vowel:
        count +=1
print(count)