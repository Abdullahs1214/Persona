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
"""
a = input("")
print(a[1:(len(a)-1)])
"""
#6.2.4
#1
"""
x = input("type a number: ")
print(int(x)+5)
"""
#2
"""
x = input("type a decimal: ")
print(abs(float(x))
"""
#3
"""
x = input("type a decimal: ")
y = input("type a decimal: ")
z = max(x,y)
print(z)
"""
#3a
"""
x = input("type a decimal: ")
y = input("type a decimal: ")
z = min(x,y)
print(z)
"""
#4
"need help"

#6.3.2
#1
"""
mylist = [0.1,2.2,5.6,7.4,9.8]
print(max(mylist))
"""
#2
"""
x =list(map(int,input("").split()))
x.reverse()
x.append(3)
del x[0]
x.extend([1,2,3])
x.append((int(x[0])+int(x[1])))
x.reverse()
print(x)
"""
#3
"""
x  = [int(i) for i in input().split ()]
print(max(x))
"""
#4
x = input().split()

a = x[0]
b = x[len(x)-1]

print(a, b)
x.insert(0,b)
#del x[1]
x.insert(len(x)-1,a)
#del x[len(x)-1]

print(x)