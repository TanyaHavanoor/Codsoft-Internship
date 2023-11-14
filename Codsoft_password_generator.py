#RANDOM PASSWORD GENERATOR

import random
import string

L=""
L+=string.ascii_letters
L+=string.digits
L+=string.punctuation

print("*****************************PASSWORD GENERATOR*******************************")
len_of_pswd=int(input("Enter the length of the password: "))
pswd=""
for i in range(len_of_pswd):
    pswd+=L[random.randint(0,((len(L))-2))]

print("The randomly generated password is:",pswd)
