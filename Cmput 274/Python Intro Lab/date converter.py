x = input("Year, Month, Day: ").split()
x[0], x[2] = x[2], x[0]
x[0], x[1] = x[1], x[0]
print("the new format is",x[0], x[1], x[2], sep=".",end =".")