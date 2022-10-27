from random import randint
# here are the six outcomes

outcomes = ["1","2","3","4","5","6"]
# generate the pseudo - random number
#number = randint (0 ,5)
# change this to print the outcome string instead of the number
# you will need to add conditional statements here
# eg , if number == 1...
index1 = randint(0,len(outcomes)-1)
print(outcomes[index1])
print(index1)