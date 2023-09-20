n = int(input())
y = list(map(int,input().split()))

profit = 0
min = y[0]
print(min)
print(range(len(y)))
for i in range(len(y)):
    dmoney = 0
    if y[i] < min:
        mvalue = y[i]

    else:
        dmoney = y[i] - min
        if dmoney > profit:
            profit = dmoney
print(profit)




