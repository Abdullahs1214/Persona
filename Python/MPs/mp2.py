#x = input("type an integer ")
y = list(input("type accidentals: "))
count3 = 0
countb = 0
for i in y:
    if i == ("#"):
        count3 = count3 + 1
    elif i in ("b"):
        countb += 1
if count3 > countb:
        a = count3-countb
        print("#"*a)
elif countb > count3:
        b = countb-count3
        print("b"*b)
elif count3 == countb:
    print("0")

