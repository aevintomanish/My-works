import pickle
l1=[]
l2=[]
l3=[]
prev=''
with open('newdata.txt',"wb") as file2:
    with open('data.txt') as file:

        data=file.readlines()
        for line in data:
            c=1
            for buf in line:
                if(buf.isspace() and c==1):
                    l1.append(prev)
                    c+=1
                    prev=''
                elif(buf.isspace() and c==2):
                    l2.append(prev)
                    c+=1
                    prev=''
                elif(buf=='\n' and c==3):
                    l3.append(prev)
                    prev=''
                else:
                    prev+=buf



    pickle.dump(l1,file2)
    pickle.dump(l2,file2)
    pickle.dump(l3,file2)
print("complete..... saving")
#read it
file = open("newdata.txt","rb")

print(pickle.load(file))
print(pickle.load(file))
print(pickle.load(file))

        
        
           
            
