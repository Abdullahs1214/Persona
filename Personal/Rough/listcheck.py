
"""
from random import randint
lista = []
listodd = []
listeven = []

b = 0

while True:
    x = randint(0,9)
    lista.append(x)
    if len(listodd) or len(listeven) >= 3:
        break
for index in lista:
    if index % 2 != 0:
        listodd.append(index)
        if len(listodd) >= 3:
            b = 1
    elif index % 2 == 0:
        listeven.append(index)
        if len(listeven) >= 3:
            b = 1
    if b == 1:
        break            
print(lista, listeven, listodd, sep="\n")

"""
nums = [3,2,4]
target = 6
for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    c = [i,j]
print (c)