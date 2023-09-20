# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER


def validate(password):
    #creating a list to store and seeing it if passes the criteria for the password
    flagmap = [0]*4 
    
    if len(password) < 8:
        return "Invalid"
    
    for character in password:
        if character in list(" @#"):
            return "Invalid"
        
        if character in list("QWERTYUIOPASDFGHJKLZXCVBNM"):
            flagmap[0] = 1
        if character in list("qwertyuiopoasdfghjklzxcvbnm"):
            flagmap[1] = 1
        if character in list("1234567890"):
            flagmap[2] = 1
        if character in list("!-$%&'()*+,./:;<=>?_[]^`{|}~"):
            flagmap[3] = 1
    if sum(flagmap) < 4:
        return "Insecure"
    else: return "Secure"






def generate(n):
    #imports a library of functions and subfunctions
    import random



if __name__ == "__main__":
    """password = input("Insert A Password ")
    print(validate(password))"""
    """neighbor = input("n: ")
    print(generate(neighbor))"""


    import random
    import string
    #converting the string to an integer
    n = int(n)
    if n <= 8:
        n = 8
    #initiating the whileloop
    confirm = "cmd"
    while confirm != "Secure":
        password = ''.join(random.choice(string.printable) for i in range(n))
        confirm = validate(password)
    return password

