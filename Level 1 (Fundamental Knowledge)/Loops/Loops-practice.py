"""
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two integers, 
A and B. given two integers A and B, write a program to add these two numbers and output the sum.
Input : 3, 1 2, 100 200, 10 40
Output: 3, 300, 50
"""
T = int(input())

while T != 0:
    a, b = map(int, input().split())
    print(a + b)
    T -= 1

# for loop

for i in range(int(input())):
    a, b = map(int, input().split())
    print(a + b)

"""
Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once. They consider a turn to be good 
if the sum of the numbers on their dice is greater than 6. Given that in a particular turn Chef and Chefina got X and Y on 
their respective dice, find whether the turn was good.
Input: 4, 1 4, 3 4, 4 2, 2 6
Output: NO, YES, NO, YES
"""
T = int(input())

while T != 0:
    x, y = map(int, input().split())
    if (x + y > 6):
        print("YES")
    else:
        print("NO")
    T -= 1 

# for loop

for i in range(int(input())):
    x, y = map(int, input().split())
    if (x + y > 6):
        print("YES")
    else:
        print("NO")
    
"""
Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day. Chef drank X ml 
of water today. Determine if Chef followed the doctor's advice or not. Input: 3, 2999, 1450, 2000. Output: YES, NO, YES.
"""
T = int(input())

while T != 0:
    x = int(input())
    if x >= 2000:
        print("YES")
    else:
        print("NO")
    T -= 1

# for loop

for i in range(int(input())):
    x = int(input())
    if x >= 2000:
        print("YES")
    else:
        print("NO")

"""
Chef wants to appear in a competitive exam. To take the exam, there are following requirements: Minimum age limit is X. (>= X)
Age should be strictly less than Y. (< Y) Chef's current Age is A. Find whether he is currently eligible to take the exam or not.
input is X Y A. Input: 5, 21 34 30, 25 31 31, 22 29 25, 20 40 15, 28 29 28. Output: YES, NO, YES, NO, YES.
"""
for i in range(int(input())):
    a = list(map(int,input().split()))
    if a[2] >= a[0] and a[2] < a[1]:
        print('YES')
    else:
        print('NO')

# while loop
T = int(input())

while T != 0:
    a = list(map(int,input().split()))
    if a[2] >= a[0] and a[2] < a[1]:
        print('YES')
    else:
        print('NO')
    T -= 1

"""
Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins. What is the 
total amount of money that Chef will have to pay? Input: 4, 1 10, 1 15, 2 10, 2 15. Output: 10, 15, 20, 30.
"""
t = int(input())
for i in range(t):
    X,Y= map(int,input().split())
    m=X*Y
    print(m)

# while loop
T = int(input())
while T != 0:
    X,Y= map(int,input().split())
    m=X*Y
    print(m) 
    T -= 1

"""
Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty and 1 bun. Find the maximum number of burgers that Chef 
can make. Input: 4, 2 2, 2 3, 3 2, 23 17. Output: 2, 2, 2, 17.
"""
t=int(input())
for i in range(t):
    a,b = map(int, input().split())
    if a<=b:
        print(a)
    else: 
        print(b)

# while loop
t=int(input())
while t != 0:
    a,b = map(int, input().split())
    if a<=b:
        print(a)
    else: 
        print(b)
    t -= 1

"""
Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X centimeters and Bob's height is Y 
centimeters. Help Charlie decide who is taller. It is guaranteed that X!=Y.
Input: 2, 150 160, 160 150. Output: B, A.
"""
for i in range(int(input())):
    A,B=map(int,input().split())
    if A>B:
        print('A')
    else:
        print('B')

# while loop
t=int(input())
while t != 0:
    A,B=map(int,input().split())
    if A>B:
        print('A')
    else:
        print('B')
    t -= 1

"""
Chef's son wants to go on a roller coaster ride. The height of Chef's son is X inches while the minimum height required is H inches. Determine whether he can go on the ride or not. Input: 4, 15 20, 50 48, 32 32, 38 39. Output: NO, YES, YES, NO.
"""
n = int(input())

for i in range(n):
    X, Y = map(int, input().split())
    
    if X >= Y:
        print("YES")
    else:
        print("NO")

"""
Chef took X dollars with him, and was quite sure that this would be enough to pay the bill. At the end, the waiter brought 
a bill of Y dollars. Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend 
and leave a bad impression on her.
"""
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(c<=b):
        print('Yes')
    else:
        print('No')

# while loop
T = int(input())
while (T != 0):
    b,c=map(int,input().split())
    if(c<=b):
        print('Yes')
    else:
        print('No')
    T -= 1

"""
Harsh was recently gifted a book consisting of N pages. Each page contains exactly M words printed on it. As he was bored, 
he decided to count the number of words in the book. Help Harsh find the total number of words in the book.
"""
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    print(N * M)

# while loop
A = int(input())
while A != 0:
    N,M=map(int,input().split())
    print(N * M)
    A -= 1

"""
Declare a variable a and initialize it to 0. Use the syntax above to create a loop, output the following to the console.
Print a in separate lines as long as it is less than 7. Increment a by 1 in each iteration.
"""
a = 0
while a < 7:
    print(a)
    a += 1

# Write a program to calculate the square and cube of numbers 2, 3, and 4.
for i in range(2, 5):
    print(i ** 2)
    print(i ** 3)


