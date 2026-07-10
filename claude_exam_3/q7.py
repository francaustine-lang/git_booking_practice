#Q7. Use a loop to count how many words are in this sentence:
#sentence = "Python loops are fun and powerful"
sentence = "Python loops are fun and powerful"
count = 0
for words in sentence.split():
    count += 1
print(count)
    
