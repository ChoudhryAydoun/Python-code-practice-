class character():
    #Private Name : String
    #Private Xposition :Integer
    #Private Yposition :Integer
    def __init__(self , name ,xpos , ypos):
        self.__Name = name 
        self.__Xposition = xpos
        self.__Yposition = ypos
    def GetXposition (self):
        return self.__Xposition
    def GetYposition(self):
        return self.__Yposition
    

    def SetXposition (self , value):
        self.__Xposition = value + self.__Xposition
        if self.__Xposition > 10000:
            self.__Xposition = 10000#limited means to limit it till 10000 so set assign it to 10000.
        elif self.__Xposition < 0 :
            self.__Xposition = 0
           
    def SetYposition(self , number):
        self.__Yposition = number + self.__Yposition 
        if self.__Yposition > 10000:
            self.__Yposition = 10000 #limited means to limit it till 10000 so set assign it to 10000.
        elif self.__Yposition < 0:
            self.__Yposition = 0

    def Move (self, direction ):# whenever he says parameter take a parameter never right string value inside finction bcuz it 
        #cannot so always rite parameter and match it with strins enter in the question.
        if direction.lower() == "up" :
            self.SetYposition(10)# Q said (use approperiate method to change postiton) 
            #value to change dont use self.__Ypsoition or Xposition or getter function use set only to change.
        elif direction.lower() == "down":
            self.SetYposition(-10)
        elif direction.lower() == "left":
            self.SetXposition(-10)
        elif direction.lower() == "right":
            self.SetXposition(10)
           
jack = character("Jack" , 50 , 50)

class Bikecharacter(character):
    #Private Name : String
    #Private Xposition :Integer
    #Private Yposition :Integer
    def __init__(self , name , xpos ,ypos):
        super().__init__(name,xpos,ypos)# init mai __ front and back both pai lagani hai remember  i forgot it 

        
    def Move (self,direction):
        #super().Move() # dont do this
        if direction.lower() =="up":
            super(). SetYposition(20)#we dont use notes polymorphism example because it is conditionalstatment so not def.super().
        elif direction.lower() == "down":
            super().SetYposition(-20)
        elif direction.lower() == "left":
            super().SetXposition(-20)
        elif direction.lower() == "right":
            super().SetXposition(20)

karla = Bikecharacter("karla", 100 , 50)


userinput = input("Enter the cahracter:")
usermove = input("enter the direction:")
if userinput.lower() == "jack":
    jack.Move(usermove)
    x = jack.GetXposition()
    y = jack.GetYposition()
    print(userinput,"new position is , X =",x,"Y =", y )
elif userinput.lower() == "karla":
    karla.Move(usermove)
    x2 = karla.GetXposition()
    y = karla.GetYposition()
    print(userinput , "new position is , X =", x2 , "Y = ", y)
