fin = open("worksheet8.py", "r")
alist = fin.read().splitlines()
for line in alist:
    print(line)
fin.close()