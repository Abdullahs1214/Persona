#1
"""
dict = {
    ""Xiao Long Bay": "China",
    "Pizza": "Italy",
    "Poutine": "Canada",
    "Toad in a Hole": "England",
    "Haggis": "Scotland"

}

print(dict)
"""
#2
dict = {
    "Canada":["Alberta","bc"],
    "USA":["California","New York"],
    "UK":["England","Wales"],
    "Italy":["Calabria","Liguria"],
    "Netherlands":["Zeeland"]
}

print(dict)
w = int(input("0-4: "))
if w == 0:
    key = "Canada"
elif w == 1:
    key ="USA"
elif w == 2:
    key = "UK"
elif w == 3:
    key = "Italy"
elif w == 4:
    key = "Netherlands"


x = int(input("0 to add values, 1 to delete values, 2 to delete key pair: "))
if x == 0:
    y = input("Add Value: ")
    dict[key].extend([y])
#elif x == 1:
#    y = input("Del Value: ")
#    dict[key].remove(["y"])
#print(dict)
elif x == 2:
    del dict[key]
print(dict)