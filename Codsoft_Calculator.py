#SIMPLE CALCULATOR

def operation(a,b):
    #function evaluates the expression using 'eval' 
    op=input("Enter the operator:")
    res=a+op+b
    final_res=eval(res)  #evaluates the expression and gives the result
    return final_res


#__MAIN__

print()
print("*********************************MENU************************************")
while True:
    print()
    ch=input("Enter 'y' to evaluate arithmetic expression or 'n' to stop.\nEnter your choice: ")
    if ch==('y' or 'Y'):
        a=input("Enter a number: ")
        b=input("Enter another number: ")
        result=operation(a,b)  #calling function
        print("The result is",result)

    elif ch==('n' or  'N'):
        print("Exiting!")
        break
    else:
        print("Error! Please enter valid input")
        print()
        
