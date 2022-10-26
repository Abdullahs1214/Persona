#1
"""
x = input("")
print(x.count("6"))
"""
#2
"""
x = input("")
if x.count("6") > 0:
    print(True)
else: print(False)
"""
#3
"""
x = input("")
print(x.replace("c","g"))
"""
#4
"""
x = input("")
if (x[0].isupper()) == True:
     print("Yes")
else: print("No")

if x[(len(x)-1)].islower() == True:
     print("Yes")
else: print("No")
"""
#5 way1
"""
x = input("")
a = x[0]
b = x[len(x)-1]
c = sum(x[1])
"""
#5 way2
"""
x = input("")
print(x[0],x[len(x)-1],sep="")
"""
#5a
a = input("")
print(a[1:(len(a)-1)])

