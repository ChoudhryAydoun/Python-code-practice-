class TreasureChest():
    #PRIVATE question: STRING
    #PRIVATE answer: INTEGER
    #PRIVATE points: INTEGER
    def __init__(self,question,ans,points):
        self.__question = question
        self.__answer = ans
        self.__points = points

    def getquestion(self):
        return self.__question
        
    def checkanswer(self,userans):
        if userans == self.__answer:
            return True
        else:
            return False
            
    def getpoints(self , attempt):
        if attempt == 1 :
            return int(self.__points)
        elif attempt == 2 :
            return (int(self.__points) // 2)
        elif attempt == 3 or attempt == 4 :
            return (int(self.__points) // 4)
        else:
            return 0

# Creating A Question Treasure
# Make A Game In Which You Show The Question To Player
# Player Keeps trying again and again to answer
# Calculate his attempts and print how many points he got
# I am not aware how many tries a Player will take to ans
# so i can not use for loop 
question = input("Enter hte question:")
answer = int(input("Enter the ans:"))
points = int(input("Enter the points:"))
myquestionchest = TreasureChest(question,answer,points)
userattempts = 0
flag = False
while flag == False:
    Q = myquestionchest.getquestion()
    print("the question is :",Q)
    useranswers = int(input("enter hte number:"))
    userattempts = userattempts + 1
    if myquestionchest.checkanswer(useranswers) == True:
        flag = True
#CAlculating points
userpoints = myquestionchest.getpoints(userattempts)
print("You got ", userpoints, "Points")

#thsi for showing how to calcualte raduis and declare onject in class it i another code from assignment just check readius *part.
#def CalculateArea(self):
#      area = 3.14 * self.__Radius * self.__Radius
#      return area