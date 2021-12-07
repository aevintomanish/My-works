filename_1=input("file name to be readed")
filename_2=input("file name to be copied")
with open (filename_1) as file1:
    with open(filename_2,"w")as file2:
            buf=file1.readlines()
            for i in buf:
                if(i!="\n"):
                    file2.write(i)
                    
           
          
print("compleleted.....")        
