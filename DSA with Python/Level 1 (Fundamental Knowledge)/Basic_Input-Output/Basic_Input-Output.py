#. Print out number 42
print(42)

# take 123 as input and otput 123 on command line
a = input("Enter the number: ")
print(a)

# input two integers and print out the sum
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = (a + b)
print(c)


'''
Chef has invented 1-minute Instant Noodles. As the name suggests, each packet takes exactly 1 minute to cook. 
Chef's restaurant has 7 stoves and only 1 packet can be cooked in a single stove at any minute. How many customers 
can Chef serve in 3 minutes if each customer orders exactly 1 packet of noodles?
input: 3 7, single line input
output: 21
a, b = map(int, input().split())
c = a * b
print (c)
''' 
a = int(input("enter the stoves you have: ")) # stoves
b = int(input("enter the total time you have: ")) # total time
# if 7 stoves cook 1pack per minute then howmany packets will be cooked in 3 minutes?
c = a * b
print (c)

'''
if there are 4 languages then there are 8 courses write a code that takes number of languages as input and outputs the courses.
'''
a = int(input("Enter number of Languages: "))
b = a * 2
print(b)

# find the area (l * b) and perimeter (2 * (l + b)) of the rectangle with sides of 11 and 13.
a = 11 * 13
b = (2 * (11 + 13))
print(f"The permiters of rectangle is {b} and area {a}")

# write a print command the prints out Hello and python in different line
print("Hello \n Python")

# inserting text in between of output (conacatination: + won't work here, only for variables)
print(3, "plus", 4, "is equsl to ", 7)

# Declare an integer variable num. Try taking a number from the console and assign it to num. Output num to the console.
num = int(input())
print(num)

"""
Create a calculator. Initialize the variables a and b based on two user inputs. Declare an integer variable sum 
and store the value of addition of a and b. Declare an integer variable diff and store the value of subtraction of a and b
Output sum and diff to the console on separate lines.
"""
a = int(input())
b = int(input())
sum = a + b
diff = a - b
print(sum)
print(diff)

# Declare a string variable x. Accept a text user input and store it in x. Output and print to the console Hello before the user defined name.
x = input()
print("Hello ", x)
