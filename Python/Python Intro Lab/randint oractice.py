from random import randint
x = randint(-41,41)
if -40 < x <= 0:
    print("Winter Coat")
elif 0 < x <= 10:
    print("Light Jacket")
elif 10 < x <= 20:
    print("Sweater")
elif 20 < x <= 40:
    print("Sun hat")
elif x <= -40:
    print("Not going outside")
elif x >= 40:
    print("Not Going Outside")


print(x)

"""
x = input("Input: ")
y = input("Input: ")

if len(x) > len(y):
    print(x,y,sep =" is larger than ")
elif len(y) > len(x):
    print(y,x,sep=" is larger than ")
elif len(x) == len(y):
    print("The strings are the same length")
"""