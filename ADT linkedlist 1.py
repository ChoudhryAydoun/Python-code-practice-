# RECORD DATATYPE 
# AS p2 user defined,   Multiple values with different datatypes grouped together
# Book (Record Datatpye)
# Title : STRING
# Author : STRING
# ISBN : INTEGER
class Book:
    # PUBLIC Title : STRING
    # PUBLIC Author : STRING
    # PUBLIC ISBN : INTEGER
    def _init_(self, Title, Author, ISBN):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
# DECLARE mybook : Book
mybook = Book("Papersdock", "Taha", 12345)
newbook = Book("Harry Potter", "Haha", 76534)
print(mybook.Author)

mybook.Author = "Bano"
mybook.Title = "Crash Course"
print(mybook.Author)
print(mybook.ISBN)


class node:
    #PUBLIC data : INTEGER
    #PUBLIC nextNode : INTEGER
    def _init_(self, dataP, nextNodeP ):
        self.data = dataP
        self.nextNode = nextNodeP
# Variable 
mynode = node(43, -1)

#print(mynode.data)
#print(mynode.nextNode)

# IF NEXT node value is -1 then make it 5 
if mynode.nextNode == -1:
    mynode.nextNode = 5
# Array of Nodes 
Linkedlist = [node(43, 1), node(56, 3), node(41, 0), node(65, -1)]
# Go to index position 1 and print the data
Linkedlist[3].nextNode = 3
print(Linkedlist[3].data)
print(Linkedlist[3].nextNode)
# compare if node at index position 1 have data greter than node (data) at index position 0 and print 
# haha if it is true and print "lala" if not true

if Linkedlist[1].data > Linkedlist[0].data:
    print("Haha")
else:
    print("Lala")