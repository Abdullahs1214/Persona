def count(lst,x):
    cnt = 0
    for item in lst:
        if item == x:
            cnt+= 1
    return cnt

def finddesireditem(lst):
    maxcount = 0
    max_item = ""
    for item in lst:
        cnt = count(lst,item)
        if cnt > maxcount:
            maxcount = cnt
            max_item = item
    return max_item

print(finddesireditem([1,3,7,1,3,2,3]))