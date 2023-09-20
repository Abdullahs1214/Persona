#only even
"""
for i in range(0,10,2):
    print(i)
    """
#on;y odd
"""
for i in range(0,10):
    if i % 2 != 0:
        print(i, end=" ")
"""
    
#revrese and end in same line
"""
for i in range(10,0,-1):
    print(i, end=" ")
"""
#2easy a
"""
x = [1, 2, 3, 4, 5]
for index in x:
    if index % 2 != 0:
        print(index,end=" ")
        """
#2easy b
"""
x = [1, 2, 3, 4, 5]
for index in x:
    x = str(index)
    x = x*2
    x = int((x))
    print((x))
    """
#2hardera
"""
x = input().split()
for index in x:
    x = int(index)
    if x % 2 != 0:
        print(x,end=" ")
"""

#2harderb

"""
x = input().split()
for index in x:
    x = str(index)
    x = x*2
    x = int(x)
    print(x)
"""
#3a cant get it
"""
x = input().split()
for character in x:
    if character in list("iI"):
        print("yes")
    else: print("failed")
"""
#7.4 main tasks
"""
import random
x = random.randint(0,100)
y = int(input("Guess a number: "))

print(x)
while y != x:
    if y > x:
        print("Too high, Guess again: ")
        y = int(input("Guess a number: "))
    elif y < x:
        print("Too low, Guess again: ")  
        y = int(input("Guess a number: ")) 
    
else: print("Correct")
"""
#7.4b
"""
x = range(0,100)
for index in x:
    if index % 3 == 0 and index % 5 != 0:
        print(index,end=" ")
"""
#7.4c
"""
x = range(0,100)
for index in x:
    if index % 3 == 0:
        print("Fizz",end=" ")
    if index % 5 != 0:
        print("Buzz", end=" ")
    if index % 3 == 0 and index % 5 != 0:
        print("FizzBuzz",end=" ")
        """