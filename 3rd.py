def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * fact( n - 1 )
x=int(input("enter the number to find factorial"))
print("factorial of ",x,"is",fact (x))
