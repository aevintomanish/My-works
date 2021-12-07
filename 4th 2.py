def fibonacci(n):
    if (n<0):
        return("invalid")
    if (n==0):
        return 0
    elif (n==1):
        return 1
    elif(n==2):
        return 1
    else:
      return fibonacci(n-1)+fibonacci(n-2)
    
     
            
x=int(input("enter the number "))
print(x," th fabonacci number =",fibonacci(x))
