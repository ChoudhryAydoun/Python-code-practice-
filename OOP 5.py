class Ballon():
    #PRIVATE Health :INTEGER
    #PRIVATE Colour :STRING
    #PRIVATE DefenceItem :STRING
    def __init__(self,colour,defence):
        self.__Health = 100
        self.__Colour = colour
        self.__DefenceItem = defence

    def Getdefenceitem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self, num):
        self.__Health = self.__Health + num # 
        
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else :
            return False
        
defenceitem = input("Enter the item:")
Colouritem = input("Enter the colour:")
Ballon1 = Ballon (Colouritem,defenceitem)

def Defend(ballon):
    strength = int(input("enter the strength:"))
    ballon.ChangeHealth(-strength)

    temp = ballon.Getdefenceitem()
    print(temp)

    if ballon.CheckHealth() == False:
        print("there is health remaining in baloon")
    else:
        print("No health remaining")
    return ballon

Ballon1 = Defend(Ballon1)
#########################################################################################
#Q4
class Lesson():
    #PRIVATE LessonType :STRING
    #PRIVATE Instructor :STRING
    def __init__(self,lesstype,instruct):
        self.__LessonType = lesstype
        self.__Instructor = instruct
   
    def GetLessonType(self):
        return self.__LessonType
    #question mai nahi hai yahan sai 
    def GetInstructor(self):
        return self.__Instructor
    def Setlessontype(self,newlesson):
        self.__LessonType = newlesson
    def SetInstructor(self,newinst):
        self.__Instructor = newinst
    # yahan tak nahi karnatha but practice 
    def GetFee(self,level):
        if level == "B":
            return 45
        elif level =="I":
            return 50
        elif level == "A":
            return 55
        else:
            return -1
#Declare LessonArray :Array [0:8] as Lesson        
LessonArray = []
for x in range(9):# use this array initializing with OOP only not with other programming concept or questions.
    LessonArray.append("","")# these two empty position (" "," ") are beacause of this (self,lesstype,instruct) these two atributes
# we can also do just one empty bec in ques he only ask for lessontype if it ask not one only then print all that there are in constructor brackets.    
LessonArray[2] = Lesson("Improve Your Serve","David")
myless = LessonArray[2].GetLessonType()
print (myless)
#SETTER AND GETTER DIFF:
# You can change the (Improve your server ) lessontype by using (LessonArray[2].Setlessontype("OOp class ") so now instead of it
# will be like (Lesson (OOp class , David)) set cahnge the attribute if we make any mehtod of thaat type of attribute
# getter only assign and get you value in variabale to print it as itis not any change happend