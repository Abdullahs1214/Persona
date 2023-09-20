sc = 62
fc = 58
rt = 0


scmin = sc % 60
schr = int((sc - scmin)/60)
print(schr, scmin, sep=":")

fcmin = fc % 60
fchr = int((fc - fcmin)/60)
print(fchr, fcmin, sep=":")

while rt != 48:
    sc += 62
    scmin = sc % 60
    schr = int((sc - scmin)/60)
    if schr >= 12:
        schr = schr - 12
    if schr >= 24:
        schr = schr - 24
    if schr >= 36:
        schr = schr - 36
    if schr >= 48:
        schr = schr - 48
    if schr >= 60:
       schr = schr - 60


    fc += 58
    fcmin = fc % 60
    fchr = int((fc - fcmin)/60)
    if fchr >= 12:
        fchr = fchr - 12
    if fchr >= 24:
        fchr = fchr - 24
    if fchr >= 36:
        fchr = fchr - 36
    if fchr >= 48:
        fchr = fchr - 48
    if fchr >= 60:
        fchr = fchr - 48
    rt += 1
    print(schr, scmin, sep=":")
    print(fchr, fcmin, sep=":")

