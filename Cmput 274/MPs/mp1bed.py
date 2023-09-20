def bed():
    l1 = list(map(int,input("").split()))
    l2 = list(map(int,input("").split()))
    print((l2[0]-l1[0])*(l2[1])-l1[1])
    

if __name__ == "__main__":
    b = bed()