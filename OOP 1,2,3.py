#Q1
class Player():
#PRIVATE name : STRING
#PRIVATE AGE : INTEGER
    def __init__(self, name ,age):#Example dont put age in it if question set age int the question so just declare it in model/function.
        self.__name = name
        self.__age = age

    def getage(self):      
        return self.__age
        
    def displayname(self):
        return self.__name
    
p1 =Player("Ninja" , 17)
p2 = Player("Ghost", 19)
print(p1.displayname() , p1.getage())
print(p2.getage(), p2.displayname())


#Q2
class Picture():
    #PRIVATE Description : STRING
    #PRIVATE width :INTEGER
    #PRIVATE height :INTEGER
    #PRIVATE framecolour : STRING
    def __init__(self, desc , width, height, frame):
        self.__description = desc
        self.__width = width
        self.__height = height
        self.__framecolour= frame
    
    #GETTER
    #One point CAll word in question is that calling any function in OOP or anywher
    #doesnot mean to write , print(paper.getheight() ,this means Question:Get the getheight() method
    # instead in calling you only do, paper.getheight()
    def getdescription(self):
        return self.__description
    def getheight(self):
        return self.__height
    def getwidth(self):
        return self.__width
    def getcolour(self):
        return self.__framecolour
    #SETTER
    def setdescription(self , newdesc):
        self.__description = newdesc
        
paper = Picture("good height",2,4,"BLUE") 
print(paper.getheight(),paper.getcolour()) 
#if we want to use setter function than :
paper.setdescription("it is very goood")
print(paper.getdescription())# the setter function has change the intial desc which was (good heigth)