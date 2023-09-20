x = input("Type a name: ")
y = int(input("Type an age: "))
if y < 0:
    print("Invalid age")
    
older = []
younger = []

names = ["Frodo","Samwise","Gandalf","Legolas","Gimli","Aragorn","Boromir","Merry","Pippin"]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

for i in range(len(ages)):
    if y < ages[i]:
        older.append(names[i])
    else:
        younger.append(names[i])

def older_print():
    print('ratt bhar')

def younger_print():
    print('ratt bhar')

if not older:
    younger_print()
elif not younger:
    older_print()
else:
    older_print()
    younger_print()
