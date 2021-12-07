#Find the value of nCr using function
# nCr = n! / (n – r)! r!
def combination(n,r):
    if(n>r):
        num1=1
        num2=1
        num3=1
        ex=n-r
        while(n!=0):
            num1=num1*n
            n=n-1

        while(ex!=0):
            num2=num2*ex
            ex=ex-1

        while(r!=0):
            num3=num3*r
            r=r-1


        return num1/(num2*num3)
    else:
        print("math error")

x = int(input("Enter a number (n) : "))
y = int(input("Enter a number (r) : "))

print("Number of Combinations (nCr) is ",x,"c",y ,"=",combination(x,y))
