#Good Luck! You've got this! :)
n,goal = tuple(map(int,input().split()))
num = 0
used = []
for i in range(n,0,-1):
    
    if num+i <= goal:
        num += i
        used.append(i)
used.reverse()
print(*used)
        
    
