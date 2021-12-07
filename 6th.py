st=input("enter the string")
vowels=0
qm=0
c=0
space=1
for i in st:
    if(i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u')or(i=='A')or(i=='E')or(i=='I')or(i=='U')or(i=='O'):
        vowels+=1
    elif(i=='?'):
        qm+=1
    elif(i==' '):
        space+=1
    else:
        c+=1
    
print("the number of timesvowels occurs:",vowels,"question marks occurs ",qm,"consonants",c)  
print("words present",space,)
