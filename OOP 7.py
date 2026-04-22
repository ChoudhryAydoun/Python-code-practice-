# POLYMORPHISM
# 1st Example
class Vehicle():
    def drive(self):
        print("Driving the vehicle")
        
class Car(Vehicle):
    def drive (self):
       super().drive()# the method of the parent class will as it is perform when it is called by super().(parentclassmethodname)
       print ("dirving the car")

class bike (Vehicle):
    def drive (self):
        super().drive()
        print("drivin the bike")

myvehicle = Vehicle()
myvehicle.drive()
#print(myvehicle.drive())# if we print it returns (None) at the end also.

mycar = Car()
mycar.drive()

mybike = bike()
mybike.drive()
# Polymorphism ek esa feature jis se ap same name ke methods
# use karsakte ho jo ke different behave karen ge 
# in different objects
# to implement this you use the same method name 
# in child class and modify it.

#2nd example
class shape():
    def area(self):
        print("The area of hte shape is ")

class square(shape):
    def area(self):
        super().area()
        length = float(input("Enter the lenght:"))
        myarea = length * length
        print("the area is " , myarea)

class triangle(shape):
    def area(self):
        base = float(input("enter the base:"))
        height = float(input("enter the height:"))
        myarea = 1/2 * base * height
        print("the area", myarea)
x = shape()
x.area()

mysquare = square()
mysquare.area()

mytriangle = triangle()
mytriangle.area()