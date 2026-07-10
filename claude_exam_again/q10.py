#Q10. Write a loop that reverses a string without using slicing ([::-1]) 
# or the reversed() function. Test it with text = "python".
text = 'python'
backwards = ''
for char in text:
    backwards = char + backwards

    print(backwards)