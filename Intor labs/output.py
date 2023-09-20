

"""
x = [1, 2, 3, 4, 5]
y = list(map(str, x))
print(y)
z = " ".join(y)
print(z)
"""
#alternate
"""
x = [1,2,3,4,5]
printstring = ""
for element in x:
    printstring += str(element)
    printstring += " "
print(printstring)
#alternate
x = [1,2,3,4,5]
print(*x)
"""

#6.5
x = input("Enter the date y/m/d: ").split()
x.reverse()
a = x[0]
b = x[1]
print(a,b)

x.insert(2,a)
del x[0]
printstring = ""
for element in x:
    printstring += str(element)
    printstring += "."
print(printstring)
