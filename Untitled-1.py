from tkinter import E


tcount = 0
thecount = 0
while not False:
    
    word = input("word: ")
    if word == "the":
        tcount = tcount + 1
    elif word == "The":
        thecount = thecount + 1
    print("total count %s" %(tcount))
    print("total count %s" %(thecount))
    
