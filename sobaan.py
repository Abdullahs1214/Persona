
x = input("Type a name: ")
y = int(input("Type an age: "))
if y < 0:
    print("Invalid age")
older = []
oloc = []
younger = [] 
yloc = []
o2 = []
y2 = []
 
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

for index in ages:
    if y > index:
        older.append(index)
    elif y < index:
        younger.append(index)
        
for index in older:
    oloc.append(ages.index(index))
for index in younger:
    yloc.append(ages.index(index))

for index in oloc:
    o2.append(names[index])
    
for index in yloc:
    y2.append(names[index])


    


    
#ans:
if o2 == []:
    print(x, "is", y,"years old, and they are younger than", (', '.join(y2)))
elif y2 == []:
    print( x,"is", y, "years old, and they are older than",(', '.join(o2)))
elif o2 != [] and y2 != []:
    print( x,"is", y, "years old, and they are older than",(', '.join(o2)))
    print(x, "is", y, "years old, and they are younger than",(', '.join(y2)))

