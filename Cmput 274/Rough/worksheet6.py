
import math
#1
def hypotnuese(a,o):
    h = math.sqrt(a**2 + o**2)
    print(h)

if __name__ == "__main__":
    hypotnuese(6,8)


#2
def pythago(a=0,o=0,h=0):
    if h == 0:
        h = math.sqrt(a**2 + o**2)
        print(h)
    elif a == 0:
        a = math.sqrt(h**2 - o**2)
        print(a)
    elif o == 0:
        o = math.sqrt(h**2 - a**2)
        print(o)

pythago(a=3,h=5)