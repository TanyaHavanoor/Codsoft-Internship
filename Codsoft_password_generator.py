#RANDOM PASSWORD GENERATOR

import random
import string

def create_pswd(len_of_pswd):
    #function used to generate a random password
    
    pswd=""
    for i in range(len_of_pswd):
        pswd+=L[random.randint(0,((len(L))-2))]
    return pswd



#__MAIN__

L=""
L+=string.ascii_letters
L+=string.digits
L+=string.punctuation
print("*****************************PASSWORD GENERATOR*******************************")
while True:
    print()
    a=input("Enter 'y' to generate new password or 'n' to stop.\nEnter your choice: ")
    print()
    if a==('y' or 'Y'):
        len_of_pswd=int(input("Enter the length of the password: "))
        password=create_pswd(len_of_pswd)
        print("The randomly generated password is:",password)
    elif a==('n' or 'N'):
        break
    else:
        print("Error! Please enter valid input")
        print()
        
