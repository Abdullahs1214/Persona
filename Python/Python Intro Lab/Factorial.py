def factorial(x):
    
    ans = 1
    if x == 0 or x == 1:
        ans = 1
    else:
        lists = list(range(1,x+1))
        for i in lists:
            ans *= i
    return(ans)

print(factorial(5))
