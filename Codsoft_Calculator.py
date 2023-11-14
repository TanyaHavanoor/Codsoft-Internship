
def operation(a,b):
    op=input("Enter the operator:")
    res=a+op+b
    final_res=eval(res)  #evaluates the expression and gives the result
    return final_res

print("*******************************************************")
a=input("Enter a number: ")
b=input("Enter another number: ")
result=operation(a,b)  #calling function
print("The result is",result)
