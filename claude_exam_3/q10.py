#Q10. Use a loop to remove all duplicate values from this list and print the result (without using set()): 
#items = [1, 2, 3, 2, 4, 1, 5, 3, 6]

items = [1, 2, 3, 2, 4, 1, 5, 3, 6]
a = 1
for i in items:
    if i == a:
        print(i, end = ' ')
        a += 1

result = []
for i in items:
    if i not in result:
        result.append(i)
    print(result)