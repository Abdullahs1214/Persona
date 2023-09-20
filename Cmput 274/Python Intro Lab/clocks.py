scm = 0
fcm = 0
sch = 0
fch = 0

while True:
    scm += 62
    fcm += 58
    if scm >= 60:
        sch +=1
        scm -= 60
    if fcm >= 60:
        fch +=1
        fcm -= 60
        
    if scm == fcm:
        break
slowclock = sch-12,
print(scm,fcm,sch,fch,slowclock)