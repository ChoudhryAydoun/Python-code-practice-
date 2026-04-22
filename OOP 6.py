#Inheritance Concept
#inheritance means like in real world it means property of parents kai paprrents ki inheritance bacho mai pass hoti hain 
#class sai pehlai hamesha parent exit hona lazmi hai like parent kai bagair child bornnahi ho sakta ussi tarha parent class ka
#bagair child class nahi ban sakta ban sakti hai magar it not a vise way your father have car so ude that donot try to buy on your 
#own form scratch.
class Employee():
    #Private Name : String
    #PRivate Age : Integer
    def __init__(self , name , age):
        self.__Name = name
        self.__Age = age
    def GetName (self):
        return self.__Name
    
# Child Class Inheriting Parent(Employee)
class Parttime(Employee):
    #Private Hourlyrate : Integer
    def __init__(self, name , age,  hourlyrate):
        super().__init__(name,age)# for accesing attributes you use__init if acces function then see polymorphism code of super
        self.__Hourlyrate = hourlyrate

    def dailywage(self , hoursworked):
        temp = hoursworked * self.__Hourlyrate
        return temp
    
class fulltime (Employee):
    # PRivate Monthlysal : Integer
    def __init__(self , name , age , monthlysal):
        super().__init__(name , age)
        self.__Monthlysal = monthlysal

    def yearlysal (self):
        temp = 12 * self.__Monthlysal
        return temp
    
parttime = Parttime("Bhatti" , 50 , 20)
print(parttime.GetName())
fulltimeworker = fulltime("Sheikh" , 60 , 3000)
print(fulltimeworker.GetName())
print(fulltimeworker.yearlysal())