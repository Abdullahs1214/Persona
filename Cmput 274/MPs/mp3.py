x = input("number of enemies and classes: ").split()
y = list(map(int,input("enemy attack ranges: ").split()))
z = list(map(int,input("class attack ranges: ").split()))
a = []
for index in z:
    if index > max(y):
        a.append(index)
       

if a != []:
    b = min(a)
    print("pick",b,sep=" ")
else: print("-1")