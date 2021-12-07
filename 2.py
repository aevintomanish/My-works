bookshop={}
n=int(input("enter the number of books: "))
for i in range(n):
    title=input(" book name: ")
    bookshop[title]=0
print(bookshop)
    
while (True):
    print("1.buy a book")
    print("2.Sell a book")
    print("3.Exit")
    option=int(input("Enter the option"))
    if(option==1):
        title=input("Enter the title of the book: ")
        n=int(input("Enter the number of books to be added: "))
        bookshop[title]+=n
        print(bookshop)
    elif(option==2):
        title=input("Enter the title of the book: ")
        n=int(input("Enter the number of books to be added: "))
        bookshop[title]-=n
        print(bookshop)
    elif(option==3):
        break
