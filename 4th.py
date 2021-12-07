def fabonacci(a) :
    n1=0
    n2=1
    n3=0
    count=0
    while (count<a):
      print (n1)
      n3= n1 + n2       
      n1 = n2
      n2 = n3
      count += 1
    
     
            
x=int(input("enter the number upto which fabonacci series to be find"))
print("fabonacci till ",x,":")            
print(fabonacci(x))       
            
        
    
    
