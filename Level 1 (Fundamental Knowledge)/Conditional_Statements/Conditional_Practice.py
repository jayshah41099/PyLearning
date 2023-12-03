"""
Let's think of a real-life example where we need to find out if a person is old enough to vote.
Find out if the age (25) is greater than OR equal to the voting age limit, which is set to 18.
"""
age = 25
vage = 18

if age >= vage:
    print("Old enough to vote!")
else:
    print("Not old enough to vote.")

# Take input for two integer variables a & b. Output "Coding is Fun" to the console if a is greater than b.
a = int(input())
b = int(input())
if a > b:
    print("Coding is Fun")

"""
Take two integers b and r as input. Print "Rob scored higher marks than Bob", if r is greater than b. 
Print "Bob & Rob both scored the same", if both b and r are equal
"""
b = int(input())
r = int(input())
if r > b:
    print("Rob scored higher marks than Bob")
elif b == r:
    print("Bob & Rob both scored the same")

"""
Create integer variables r and k the weight of friends Ram and Karan as r = 24 and k = 32. 
"Ram is heavier than Karan" if r is greater than k. "Karan is heavier than Ram" if r is lesser than k
"Ram & Karan have the same weight!" for any remaining conditions.
Update the values of r and k as r = 78 and k = 78. "Ram is heavier than Karan" if r is greater than k
"Karan is heavier than Ram" if r is lesser than k. "Ram & Karan have the same weight!" for any remaining conditions.
"""
r = 24
k = 32

if r > k:
    print("Ram is heavier than Karan")
elif r < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")
    
r = 78
k = 78

if r > k:
    print("Ram is heavier than Karan")
elif r < k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight!")

# If the score is 100, print "Perfect score". If the score is less than 100, but greater or equal to 80, 
# print "Almost perfect score". If the score is less than 80, print "Nice try".
score = int(input())
if score == 100:
    print("Perfect score")
elif score < 100 and score >= 80:
    print("Almost perfect score")
elif score < 80:
    print("Nice try")

"""
In ChefLand, human brain speed is measured in bits per second (bps). Chef has a threshold limit of X bits per second above 
which his calculations are prone to errors. If Chef is currently working at Y bits per second, is he prone to errors?
If Chef is prone to errors print YES, otherwise print NO.
"""
x, y = map(int, input().split())
if y > x:
    print("YES")
else:
    print("NO")

"""
Chef defines a pair of positive integers (a,b) to be a Oneful Pair, if a+b+(a⋅b)=111. Output Yes, if (a,b) form a Oneful Pair. 
Output No if they do not.
"""
a, b = map(int, input().split())
if ( (a + b + (a * b)) == 111):
    print("Yes")
else:
    print("No")

"""
Chef has a threshold limit of X bits per second above which his calculations are prone to errors. If Chef is currently 
working at Y bits per second, is he prone to errors? If Chef is prone to errors print YES, otherwise print NO.
"""
x,y=map(int,input().split())
if y<=x:
    print("NO")
else:
    print("YES")


