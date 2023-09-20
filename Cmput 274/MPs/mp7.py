n,m,k = tuple(map(int,input().split()))
t_i = sorted(list(map(int,input().split())))
baked = 0
l = 0
while n > l:
    baked = baked + 1
    cons = 0
    for i in t_i[l:m+l]:
        if 2*k >= i - t_i[l] >= 0:
            cons = cons + 1
    l = l + cons
print(baked)
