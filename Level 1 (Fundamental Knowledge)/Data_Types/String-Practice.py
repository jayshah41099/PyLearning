"""
Declare two variables a and b. Assign Learning to a and is fun! to b. display the sentence "Learning is fun!" 
using variables a and b in a single line.
"""
a = "Learning"
b = " is fun!"
print(a, b)

# hello World using variable x and y
x = "Hello"
y = "World"
print (x + " " + y)

# We need to output 2569 using string concatenation.
string1 = "25"
string2 = str(69)
print(string1 + string2)

"""
Create a variable txt and assign it the text NumeroTres
Use the len() function to output to the console the number of characters in txt.
"""
txt = "NumeroTres"
print(len(txt))

"""
Create a string variable word and assign the text Programming to it
Print the characters o and r from the string word in separate lines using the syntax defined above
"""
word = "Programming"
print( word[2] + "\n" + word[1])

"""
Initialize a string variable word and assign the value Ocygen to it. You now want to fix the typo in the given string.
Use the syntax explained above to replace 'c' with 'x' in a new variable word_new. Output the updated word_new to console
"""
word = "Ocygen"
word_new = word.replace(word[1], "x")
print(word_new)

"""
Declare a string variable var. Assign the value String to it. Use string slicing to print ring to the console.
"""
var = "String"
print(var[2:6])

