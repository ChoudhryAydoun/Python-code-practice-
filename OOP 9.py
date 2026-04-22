# Containment means a object with in an object object mai object mehtod mai bhi object .
class fooditem():
    #PRIVATE name : String 
    #PRIVATE code : String
    #PRIVATE cost : Real
    def __init__(self,namep , codep , costp):
        self.__name = namep
        self.__code = codep
        self.__cost = costp

    def getcode (self):
        return self.__code
    def getcost(self):
        return self.__cost
    def getname(self):
        return self.__name
    
class Vendingmachine ():
    #Private item : Array [0:3] as String (declare array like this)
    #Private moneyin :Real
    def __init__(self,item1,item2,item3 ,item4):
        self.__item = []# they were wrong because i donot include self.__ in them
        self.__item .append(item1)
        self.__item .append(item2)
        self.__item .append(item3)
        self.__item .append(item4)

        self.__moneyin = 0

    def checkvalid (self , code):
        for x in range(len(self.__item)):
            if self.__item[x].getcode() == code:#always write [x] with object self.__item not in method getcode
                if self.__item[x].getcost() <= self.__moneyin:
                    return x 
                else:
                    return -2
        return -1                           
    def insertmoney(self , paisa):
        self.__moneyin = self.__moneyin + paisa

chocolate = fooditem("dairymilk" , "2030" , 20.98)
sweet = fooditem("gulab jamun" , "2031" , 150.45)
sandwich = fooditem("buger" , "2032" , 200.30)
apple = fooditem("red" , "3409" , 25.4)
machineone = Vendingmachine(chocolate , sweet, sandwich , apple)
machineone.insertmoney(200)
temp = machineone.checkvalid("2032")
print(temp)