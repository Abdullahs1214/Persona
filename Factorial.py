def factorial(x):
    ans = 0
    if x == 0 or x == 1:
        ans = 1
    else:
        ans = x*(x-1)
    return ans

print(factorial(5))
