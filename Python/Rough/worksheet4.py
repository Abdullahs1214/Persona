def safeinput(prompt):
    try:
        word = input(prompt)
        return(word,True)
    except EOFError:
        return("",True)

count = 0
words = 0
nontarget= []
flag = True
while flag:
    word,flag = safeinput("").split()
    if flag:   
        words += 1
    if word in ["The","the"]:
        count += 1
    elif word != "":
        if word not in nontarget:
            nontarget.append(word)

print("words:%3s. Target words:%3s" %(words,count))
print("non target words: ", nontarget)







"""
theCount = 0
done = False

while not done:
    try:
        word = input("Word: ")
    except EOFError:    
        done = True
        continue
    if word in ["The","the"]:
        theCount = theCount + 1

    if word in ["exit","Exit"]:
        done = True
   
print( "Total count %s" % (theCount) )

"""






"""
count = 0
word = input("word: ")
if word in ["The","the"]:
    count += 1
print(count)

"""
"""
words = ["outside","today", "weather", "raining", "nice", "rain","snow", "day", "winter", "cold"]
totalcount = 0
word = 0
x  =[]
while word != "exit":
    
    word = input("word: ").split()
    if word in words:
        totalcount = totalcount + 1

    
    if word not in words:
        x.append(word)
print(x)
print(totalcount)
"""