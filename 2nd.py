list_1=[]
n=int(input("Enter the list size : "))
for i in range (n+1):
   x=int(input("enter the elements:"))
   list_1.append(x)
x=(int(input("enter the element your searching for ")))
if x in list_1:
    print ((list_1.index(x),"is the postion"))
else:
    print("invalide!!!!")
   

        

