n = int(input())
y = list(map(int,input().split()))
m = min(y)


a = (y.index(min(y)))
x = list(y[a:])

profit = 0
for index in x:
    if index > m:
        profit = index - min(y)
       
print(profit)
       
       

        

