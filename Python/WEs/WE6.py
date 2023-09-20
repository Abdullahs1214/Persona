n = int(input(""))
applicants = []
for i in range(0,n):
    h = int(input(""))
    applicants.append(h)

applicants.sort()
if n <= min(applicants):
    N = n
else:
    for i in range(len(applicants)):
        if n - applicants[i] >= i:
            x = i
            N = applicants[x]
        elif n - (N+1) > x:
            N = N+1
print(N)


