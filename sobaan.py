
x = input("Type a name: ")
y = int(input("Type an age: "))
if y < 0:
    print("Invalid age")
else:
    
    older = []
    younger = []

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

    for index in range(len(ages)):
        if y < ages[index]:
            older.append(names[index])
        else:
            younger.append(names[index])



#ans:

    def younger_print():
        print(x,"is", y,"years old, and they are older than", (', '.join(younger)))
    
    def older_print():
        print(x,"is", y,"years old, and they are younger than",(', '.join(older)))

    if not older:
        younger_print()
    elif not younger:
        older_print()
    else:
        younger_print()
        older_print()
