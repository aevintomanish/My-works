def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divi(a,b):
    return a/b
def exp(a,b):
    return a**b


x = int(input("enter first number:"))
y = int(input("enter  next number:"))

c=int(input("menu \n 1 : addition \n 2 : subtraction \n 3: multiplication \n 4:division \n 5:exponent"))
   
if(c==1):
   print(y,"+",x,"=",add(x,y))
   
if(c==2):
   print(x,"-",y,"=",sub(x,y))
   
if(c==3):
   print(y,"X",x,"=",mul(x,y))
   
if(c==4):
   print(x,"/",y,"=",divi(x,y))
  
if(c==5):
   print(x,"^",y,"=",exp(x,y))
   
elif(c<1 or c>5):
    print("invalide selection")
